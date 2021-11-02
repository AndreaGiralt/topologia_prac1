import scrapy, os
import pandas as pd

from libs.database import Database


class UnemploymentSpider(scrapy.Spider):

    base_url = "https://datos.gob.es/es/catalogo/ea0021425-paro-registrado-por-municipios"
    name = "unemployment"
    db = None

    def start_requests(self):

        yield scrapy.Request(
            url=self.base_url,
            callback=self.parse_response
        )

    def parse_response(self, response, **kwargs):

        selectors = response.css("a.resource-url-analytics")

        selector = selectors[-1]

        link = selector.attrib['href']

        yield scrapy.Request(
            url=link,
            callback=self.download_csv
        )

    def download_csv(self, response):

        path = response.url.split('/')[-1]
        dirf = r"data"

        if not os.path.exists(dirf):
            os.makedirs(dirf)


        complete_path =dirf+"/"+path
        with open(complete_path, 'wb') as f:
            f.write(response.body)

        self.parse_file (complete_path)

    def parse_file (self, file_path):

        db = Database()

        df = pd.read_excel(file_path,header=1)
        df_balears = df[df["Provincia"] == "Balears, Illes"]

        last_date = df_balears["mes"].unique()[-1]
        df_balears_last_date = df_balears[df_balears["mes"] == last_date]

        db.storeUnemploymentInfo(df_balears_last_date.to_dict("records"))
