# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from valerie.pages.models import Page, NameablePage

from deprecated import deprecated


class GalleryItem(NameablePage):
    content_Item = models.TextField(null=True, verbose_name="Contenu")
    position_Item = models.PositiveIntegerField(blank=True, null=True, verbose_name="Position")

    def save(self, *args, **kwargs):
        if not self.position_Item:
            item_cat = GalleryItem.objects.filter(parent=self.parent)
            if item_cat:
                self.position_Item = item_cat.order_by('position_Item').last().position_Item + 1
            else:
                self.position_Item = 0

        self.parent.type = 1
        super(GalleryItem, self).save(**kwargs)


class PhotoGallery(GalleryItem):
    photo_img = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR + '/photos')

    def __str__(self):
        return "Photo " + super(PhotoGallery, self).__str__()

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _(verbose_name + 's')


class VideoGallery(GalleryItem):
    youtube_url = models.CharField(max_length=256, verbose_name="Lien Youtube")

    def __str__(self):
        return "Vidéo " + super(VideoGallery, self).__str__()

    class Meta:
        verbose_name = _('Vidéo')
        verbose_name_plural = _(verbose_name + 's')


@deprecated
class OldPhoto(NameablePage):
    content = models.TextField(null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    photo_img = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR+'/photos')






