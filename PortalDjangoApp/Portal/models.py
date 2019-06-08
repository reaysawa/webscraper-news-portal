from django.db import models

class NewsHeading(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    read_more = models.TextField()
    banner = models.TextField()

