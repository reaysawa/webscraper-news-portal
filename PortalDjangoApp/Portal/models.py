from django.db import models


class NewsHeading(models.Model):
    """
    This model is mirrored by it's equivalent 'scrapy.Item' descendant in the
    Scrapy application.
    """

    title = models.TextField()
    subtitle = models.TextField()
    read_more = models.TextField(primary_key=True)
    banner = models.TextField()
