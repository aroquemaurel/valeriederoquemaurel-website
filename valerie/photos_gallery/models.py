# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from valerie.pages.models import Page, NameablePage

from deprecated import deprecated


class GalleryItem(NameablePage):
    # TODO AR : Categorie
    content_Item = models.TextField(null=True)
    # TODO AR : favorite home, home image, home link, utile ?
    position_Item = models.PositiveIntegerField(blank=True, null=True)

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


@deprecated
class OldPhoto(NameablePage):
    # TODO AR : Categorie
    content = models.TextField(null=True)
    # TODO AR : favorite home, home image, home link, utile ?
    position = models.PositiveIntegerField(blank=True, null=True)
    photo_img = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR+'/photos')






