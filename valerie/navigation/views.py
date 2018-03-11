# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from valerie.navigation.models import Category

# Route
def display_category(request, slug):
    slug_subcat = None

    if slug is not None:
        try:
            cat = Category.objects.get(slug=slug)

            if cat.default_child is not None:
                slug_subcat = cat.default_child.slug

        except Category.DoesNotExist:
            slug_subcat = None

    return display_subcategory(request, slug, slug_subcat)


def _display_category(request, cat):
    if cat is not None and cat.default_child is not None:
        subcat = cat.default_child
    else:
        subcat = None

    return _display_subcategory(request, cat, subcat)


def _display_subcategory(request, cat, subcat):
    return render(request, 'category_list.html', {'categories': Category.objects.filter(parent=None),
                                                      'current_cat': cat,
                                                      'current_subcat': subcat})

# Route
def display_subcategory(request, slug_cat, slug_subcat):
    try:
        cat = Category.objects.get(slug=slug_cat)
    except Category.DoesNotExist:
        cat = None

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        subcat = None

    return _display_subcategory(request, cat, subcat)


# Route
def category_list(request):
    try:
        slug_cat = Category.objects.get(home=True).slug
    except Category.DoesNotExist:
        slug_cat = ""

    return display_category(request, None)

