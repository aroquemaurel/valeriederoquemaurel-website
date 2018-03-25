# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from valerie import pages
from valerie.pages.models import Page


class Photo(pages.models.NameablePage):
    # TODO AR : Categorie
    content = models.TextField(null=True)
    # TODO AR : favorite home, home image, home link, utile ?
    position = models.PositiveIntegerField()
    # TODO AR : image

    def __str__(self):
        return self.title


