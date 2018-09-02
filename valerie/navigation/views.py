# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseNotFound
from django.shortcuts import render

import valerie

from valerie.pages import views

# Create your views here.
from valerie.navigation.models import Category


# Route
def display_category(request, slug):
    slug_subcat = None
    cat = None

    try:
        cat = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
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
        return HttpResponseNotFound('<h1>Page not found</h1>')

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    default_page = subcat.get_default_page()
    if default_page is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return valerie.pages.views.display_page(request, default_page)
