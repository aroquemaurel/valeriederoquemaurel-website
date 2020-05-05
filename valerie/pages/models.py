# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_unique_slugify import unique_slugify

logger = logging.getLogger(__name__)


class Type:
    PHOTO = 1
    CONTENT = 2
    EVENT = 3
    PRESS = 4


class Page(models.Model):
    parent = models.ForeignKey('navigation.Category',
                               null=True,
                               related_name='category_page',
                               on_delete=models.CASCADE,
                               verbose_name="Catégorie parente")
    type = models.IntegerField(default=1, verbose_name="Type de page")

    def title(self):
        if self.parent is not None and self.parent.title is not None:
            return self.parent.title

        return ""

    def slug(self):
        return self.parent.slug

    @property
    def label_type(self):
        if self.type == Type.PHOTO:
            return "Photo"
        elif self.type == Type.CONTENT:
            return "Contenu"
        elif self.type == Type.EVENT:
            return "Evenement"
        elif self.type == Type.PRESS:
            return "Presse"
        else:
            logger.error("The type of object " + self.type.__str__() + " is unknown")

        return ""

    def __str__(self):
        return self.title()

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _(verbose_name + 's')


class NameablePage(Page):
    title = models.CharField(max_length=256, verbose_name="Titre")
    slug = models.SlugField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)

        super(NameablePage, self).save(**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page nommée')
        verbose_name_plural = _('Pages nommées')
