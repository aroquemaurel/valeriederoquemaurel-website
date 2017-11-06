# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    # TODO AR : parent, null ou une autre categorie

    def __str__(self):
        return self.title
