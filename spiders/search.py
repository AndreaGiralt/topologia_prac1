import scrapy, csv, math, re

from items import RealStateItem
from libs.database import Database


class SearchSpider (scrapy.Spider):

    base_url = "https://pisos.com"
    name = "search"
    db = None

    def start_requests(self):

        self.db = Database()

        with open("data/zonas.csv") as file:

            csv_reader = csv.reader(file)
            next(csv_reader, None) #Remove headers.

            for row in csv_reader:
                print ("Processing: " + row[0] )

                total_pages = math.ceil(int(row[1])/30);

                for i in range(1,total_pages):

                    print("Page: " + str(i))

                    request_id_string = ''

                    if i > 1:
                        request_id_string = str(i)

                    detail_url = self.base_url + row[0] + request_id_string

                    yield scrapy.Request(
                        url=detail_url,
                        callback=self.parse_response,
                        meta = {
                            'page': i
                        }
                    )

                    break
                break

    def parse_response(self, response, **kwargs):

        selectors = response.css(".ad-preview")

        for selector in selectors:

            item = RealStateItem()
            item['id'] = selector.attrib['id']

            #price
            price = selector.css(".ad-preview__price::text").extract()
            if price and len(price)>0:
                item['price'] = price[0].strip()

            #title
            title = selector.css(".ad-preview__title::text").extract()
            if title and len(title) > 0:
                item['title'] = title[0].strip()
                m = re.match("^((?!en).)*", item['title'])
                if m:
                    item['type'] = m.group(0)

            #description
            description = selector.css(".ad-preview__description::text").extract()
            if description and len(description) > 0:
                item['description'] = description[0].strip()

            details = selector.css(".ad-preview__info .ad-preview__section  p.p-sm::text").extract()
            if details and len(details)>0:

                m = re.match("([^()]+) \(([^()]+)\)", details[0])
                if m:
                    item['zone'] = m.group(0)
                    item['town'] = m.group(1)
                else:
                    item['town'] = details[0]

                for detail in details[1:]:
                    if re.match(r"[0-4]+ hab",detail):
                        item['rooms'] = detail
                    elif re.match(r"[0-4]+ m",detail):
                        item['surface'] = detail
                    elif re.match(r"[0-4]+ ba",detail):
                        item['bathrooms'] = detail
                    else:
                        item['floor'] = detail

            self.db.store_item(item)
