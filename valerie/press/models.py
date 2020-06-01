# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from valerie.common.models import ImageAttachment, Attachment


class Article(models.Model):
    date = models.DateField(verbose_name="Date de l'article")
    title = models.CharField(max_length=256, verbose_name="Titre")
    content = models.TextField(null=True, blank=True, verbose_name="Description")
    youtube_link = models.CharField(max_length=256, null=True, blank=True, verbose_name="Lien Youtube")

    def get_images(self):
        return self.article_attachment_image.all().order_by('position')

    def __str__(self):
        return "Article " + self.title + " du " + self.date.strftime('%d %b %Y')

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _(verbose_name + 's')


class ImageAttachmentArticle(ImageAttachment):
    def folder_name(self):
        return "presse"

    article = models.ForeignKey('press.Article',
                                null=True,
                                related_name='article_attachment_image',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _(ImageAttachment.verbose_name)
        verbose_name_plural = _(ImageAttachment.verbose_name_plural)
