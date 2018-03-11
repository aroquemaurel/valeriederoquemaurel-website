# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=100)
    # Si aucun parent, catégorie, sinon sous-catégorie.
    parent = models.ForeignKey('Category', null=True, related_name='parent_cat')
    default_child = models.ForeignKey('Category', null=True, related_name='default_child_subcat')
    home = models.BooleanField(default=False)

    # Retourne les sous-catégories de la categorie courante
    def get_childs(self):
        return self.parent_cat.all()


    def __str__(self):
        return self.title

