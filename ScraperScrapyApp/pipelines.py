# -*- coding: utf-8 -*-

from Portal import models as PortalDjangoAppModels


class NewsHeadingPipeline(object):
    items = []

    def close_spider(self, spider):
        """Stores every item in one go after crawling is done"""
        if self.items:
            PortalDjangoAppModels.NewsHeading.objects.bulk_create(self.items)

    def process_item(self, item, spider):
        """Batches items to save SQL-query insertion times"""
        self.items.append(item)
        return item
