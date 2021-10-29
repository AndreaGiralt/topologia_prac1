import scrapy, csv

class ZonesSpider(scrapy.Spider):

    base_url = "https://www.pisos.com/"
    name = "zones"

    def start_requests(self):

        detail_url = self.base_url + "/viviendas/isla_de_mallorca/"

        yield scrapy.Request(
            url=detail_url,
            callback=self.parse_response
        )

    def parse_response(self, response, **kwargs):

        selectors = response.css(".item-subitem")

        with open("data/zonas.csv", "w") as file:

            csv_file = csv.writer(file)
            csv_file.writerow(['zone','total'])

            for selector in selectors:
                href = selector.attrib['href']
                total = selector.css(".total::text").extract()[0] #cogemos los totales.
                csv_file.writerow([href,total.strip("()")])









