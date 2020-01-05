# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="Titre")
    slug = models.SlugField(max_length=100)
    # Si aucun parent, catégorie, sinon sous-catégorie.
    parent = models.ForeignKey('Category', null=True, related_name='parent_cat',
                               on_delete=models.CASCADE, verbose_name="Catégorie parente")
    default_page = models.ForeignKey('pages.Page', null=True, related_name='default_page',
                                     on_delete=models.CASCADE, verbose_name="Page par défaut")
    img_mini = models.ImageField(upload_to=settings.UPLOAD_RELATIVE_DIR + '/categories', null=True, verbose_name="Miniature")

    def get_pages(self):
        return self.category_page.all()

    def get_default_page(self):
        page = self.default_page
        if page is None:
            all_pages = self.get_pages()

            if all_pages.count() > 0:
                page = all_pages[0]

        if page is None:
            # TODO AR : on retourne une 404
            return None

        return page

        # Retourne les sous-catégories de la categorie courante

    def get_childs(self):
        return self.parent_cat.all()

    def __str__(self):
        if self.title is not None:
            return self.title

        return ""

    class Meta:
        verbose_name = _('Catégorie')
        verbose_name_plural = _(verbose_name + 's')

