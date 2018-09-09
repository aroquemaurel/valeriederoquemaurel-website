# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from valerie.navigation.models import Category
from valerie.pages.models import Page
from valerie.press.models import Article


def display_articles(request, page_id):
    current_page = Page.objects.get(id=page_id)
    articles = Article.objects.all()

    return render(request, 'events/display-events.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_page.parent.parent,
                      'current_subcat': current_page.parent,
                      'page': current_page,
                      'articles': articles
                  })


