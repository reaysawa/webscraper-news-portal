# -*- coding: utf-8 -*-

import ScraperScrapyApp.pipelines.django_setup
from PortalDjangoApp.Portal import models as PortalDjangoAppModels


class NewsHeadingPipeline(object):
    """
    Pipeline for accumulating only news titles from websites
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
                title=item["title"],
                subtitle=item["subtitle"],
                read_more=item["read_more"],
                banner=item["banner"],
            )
        )
        return item
