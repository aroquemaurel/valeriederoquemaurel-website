# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponseNotFound
from django.shortcuts import render

import valerie

from valerie.pages import views

# Create your views here.
from valerie.navigation.models import Category


logger = logging.getLogger(__name__)


def display_category(request, slug):
    slug_subcat = None
    cat = None

    try:
        cat = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        logger.error("The category "+slug+" is not found")
        cat = None
    # TODO AR : 404

    # On a pas d'enfants, on prends la page par défaut
    if slug_subcat is None and cat.get_childs().count() == 0:
        return valerie.pages.views.display_page(request, cat.get_default_page())

    # On a des enfants, on affiche la catégorie
    return render(request,  'navigation/display_category.html', {
                                'categories': Category.objects.filter(parent=None),
                                'current_cat': cat
                            })


# Route
def display_subcategory(request, slug_cat, slug_subcat):
    try:
        cat = Category.objects.get(slug=slug_cat)
    except Category.DoesNotExist:
        logger.error("The category " + slug_cat + " is not found")
        return HttpResponseNotFound('<h1>Page not found</h1>')

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        logger.error("The subcategory " + slug_subcat + " is not found")
        return HttpResponseNotFound('<h1>Page not found</h1>')

    default_page = subcat.get_default_page()
    if default_page is None:
        logger.error("The default page of " + slug_subcat + " is not found")
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return valerie.pages.views.display_page(request, default_page)
