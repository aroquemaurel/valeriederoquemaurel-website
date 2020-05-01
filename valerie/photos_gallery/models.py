# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from valerie.pages.models import Page, NameablePage


class Photo(NameablePage):
    # TODO AR : Categorie
    content = models.TextField(null=True)
    # TODO AR : favorite home, home image, home link, utile ?
    position = models.PositiveIntegerField(blank=True, null=True)
    photo_img = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR+'/photos')

    def save(self, *args, **kwargs):
        if not self.position:
            photos_cat = Photo.objects.filter(parent=self.parent)
            if photos_cat:
                self.position = photos_cat.order_by('position').last().position + 1
            else:
                self.position = 0

        self.parent.type = 1
        super(Photo, self).save(**kwargs)

    def __str__(self):
        return "Photo " + super(Photo, self).__str__()


