# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Type:
    PHOTO = 1
    CONTENT = 2
    EVENT = 3


class Page(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey('navigation.Category', null=True, related_name='category_page')
    type = models.IntegerField(default=1)

