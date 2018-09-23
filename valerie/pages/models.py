# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Type:
    PHOTO = 1
    CONTENT = 2
    EVENT = 3
    PRESS = 4


class Page(models.Model):
    parent = models.ForeignKey('navigation.Category', null=True, related_name='category_page',
            on_delete=models.CASCADE)
    type = models.IntegerField(default=1)

    def title(self):
        return self.parent.title

    def slug(self):
        return self.parent.slug


class NameablePage(Page):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title




