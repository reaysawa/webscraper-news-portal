from scrapy import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose

from ScraperScrapyApp.items import NewsHeading

class TecMundoSpider(Spider):
    name = "TecMundoSpider"

    def __init__(self, env='PROD'):
#         if env == 'PROD':
            # self.allowed_domains = ["tecmundo.com.br"]
            # self.start_urls = ["https://tecmundo.com.br"]
        # else:
        self.start_urls = ["http://localhost:8080"]

        # item parsing
        self.item_field_path = '//*[@id="carousel-tv"]/div/a'
        self.item_fields = {
            "title": ".//@title",
            "read_more": ".//@href",
            "banner": './/img[@class="nzn-main-img"]/@src',
            "subtitle": './/div[@class="nzn-main-text"]/strong/text()',
        }

    def parse(self, response):
        for heading in response.xpath(self.item_field_path):
            loader = ItemLoader(NewsHeading(), selector=heading)

            loader.default_input_processor = MapCompose(str.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
