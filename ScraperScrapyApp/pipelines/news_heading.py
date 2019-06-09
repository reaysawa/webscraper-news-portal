# -*- coding: utf-8 -*-

import ScraperScrapyApp.pipelines.django_setup
from PortalDjangoApp.Portal.models import NewsHeading


class NewsHeadingPipeline(object):
    """
    Pipeline for accumulating only news titles from websites
    """

    items = []
    allowed_fields = set([f.name for f in NewsHeading._meta.get_fields()])

    def close_spider(self, _spider):
        """Stores every item in one go after crawling is done"""
        if self.items:
            current_set = {news.read_more: news for news in NewsHeading.objects.all()}

            create_batch = [
                item for item in self.items if item["read_more"] not in current_set
            ]
            if create_batch:
                NewsHeading.objects.bulk_create(
                    [
                        NewsHeading(
                            **{
                                k: v
                                for k, v in item.items()
                                if k in self.allowed_fields
                            }
                        )
                        for item in create_batch
                    ]
                )

            update_batch = [
                item for item in self.items if item["read_more"] in current_set
            ]
            if update_batch:
                self.allowed_fields.remove("read_more")
                for item in update_batch:
                    for k, v in item.items():
                        if k in self.allowed_fields:
                            setattr(current_set[item["read_more"]], k, v)

                NewsHeading.objects.bulk_update(
                    current_set.values(), list(self.allowed_fields)
                )

    def process_item(self, item, _spider):
        """Batches items to save SQL-query insertion times"""
        self.items.append(item)
        return item
