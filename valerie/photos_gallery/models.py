# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Photo(models.Model):
    # TODO AR : Categorie
    title = models.CharField(max_length=256)
    content = models.TextField(null=True)
    # TODO AR : favorite home, home image, home link, utile ?
    position = models.PositiveIntegerField()
    # TODO AR : image

    def __str__(self):
        return self.title


