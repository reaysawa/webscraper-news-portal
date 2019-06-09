# -*- coding: utf-8 -*-

from PortalDjangoApp.Portal import models as PortalDjangoAppModels


class NewsHeadingPipeline(object):
    """
    Generic pipeline which batches Scrapy items and does insertion in bulks
    """

    items = []

    def close_spider(self, spider):
        """Stores every item in one go after crawling is done"""
        if self.items:
            PortalDjangoAppModels.NewsHeading.objects.bulk_create(self.items)

    def process_item(self, item, spider):
        """Batches items to save SQL-query insertion times"""
        self.items.append(
            PortalDjangoAppModels.NewsHeading(
                title=item.title.__str__(),
                subtitle=item.subtitle.__str__(),
                read_more=item.read_more.__str__(),
                banner=item.banner.__str__(),
            )
        )
        return item
