from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import NewsHeading


class TecMundoSpider(BaseSpider):
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
            loader = XPathItemLoader(NewsHeading(), selector=heading)

            loader.default_input_processor = MapCompose(str.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
