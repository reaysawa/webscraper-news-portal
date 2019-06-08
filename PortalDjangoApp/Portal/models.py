from django.db import models

class NewsHeading(models.Model):
    title = models.CharField()
    subtitle = models.CharField()
    read_more = models.CharField()
    banner = models.CharField()

