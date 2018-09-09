# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from valerie import settings


class Article(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=256)
    content = models.TextField(null=True)


class ImageArticle(models.Model):
    img = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR + '/presse')
    position = models.PositiveIntegerField()
    article = models.ForeignKey('press.Article', null=True, related_name='article_image')

