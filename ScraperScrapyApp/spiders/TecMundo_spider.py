from scrapy import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose

from ScraperScrapyApp.items import NewsHeading


class TecMundoSpider(Spider):
    name = "TecMundoSpider"
    allowed_domains = ["https://tecmundo.com.br"]
    start_urls = ["https://www.tecmundo.com.br/"]

    # item parsing
    item_field_path = '//*[@id="carousel-tv"]/div[1]/a'
    item_fields = {
        "title": ".//[@title]",
        "read_more": ".//[@href]",
        "banner": './/img[@class="nzn-main-img"]',
        "subtitle": './/div[@class="nzn-main-text"]/strong',
    }

    def parse(self, response):
        selector = HtmlXPathSelector(response)

        for heading in selector.select(self.item_field_path):
            loader = ItemLoader(NewsHeading(), selector=heading)

            loader.default_input_processor = MapCompose(str.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
