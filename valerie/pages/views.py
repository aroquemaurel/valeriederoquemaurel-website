# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from valerie.navigation.models import Category
from valerie.pages.models import Type, Page


def home(request):
    try:
        cat = Category.objects.get(slug="accueil")  # TODO AR : config ?
    except Category.DoesNotExist:
        cat = None

    return display_page(request, cat.default_page())


def display_page(request, page):
    if page.type == Type.CONTENT:
        cat = page.parent.parent
        template_path = ""

        if cat is not None:
            template_path = cat.slug+"/"

        template_path += page.slug()

        return render(request, 'pages/content/'+template_path+'.html',
                      {
                          'categories': Category.objects.filter(parent=None),
                          'current_cat': cat,
                          'page': page
                      })

    else:
        return None


def display_category(request, cat):
    return render(request, 'pages/display_category.html', {
                            'categories': Category.objects.filter(parent=None),
                            'current_cat': cat
    })




