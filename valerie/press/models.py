# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from valerie.common.models import ImageAttachment


class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=256)
    content = models.TextField(null=True)
    youtube_link = models.CharField(max_length=256, null=True)

    def get_images(self):
        return self.article_attachment_image.all().order_by('position')


class ImageAttachmentArticle(ImageAttachment):
    def folder_name(self):
        return "presse"

    article = models.ForeignKey('press.Article', null=True, related_name='article_attachment_image', on_delete=models.CASCADE)
