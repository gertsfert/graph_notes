import datetime

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_time = models.DateTimeField("time published")
    modified_time = models.DateTimeField("last modified")

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_time >= timezone.now() - datetime.timedelta(days=1)
