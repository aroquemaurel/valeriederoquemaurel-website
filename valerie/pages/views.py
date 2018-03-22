# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from valerie.navigation.models import ParentCategory, Category
from valerie.pages.models import Type


def home(request):
    try:
        cat = ParentCategory.objects.get(is_home=True)
    except Category.DoesNotExist:
        cat = None

    return display_page(request, cat.default_page)


def display_page(request, default_page):
    if default_page.type == Type.CONTENT:
        sub_cat = default_page.parent.parent
        template_path = ""

        if sub_cat is not None:
            template_path = sub_cat.slug+"/"

        template_path += default_page.slug

        return render(request, 'pages/content/'+template_path+'.html',
                      {
                          'categories': ParentCategory.objects.all(),
                          'current_cat': default_page.parent,
                          'page': default_page
                      })

    else:
        return None
