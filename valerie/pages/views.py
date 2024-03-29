# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.shortcuts import render
import valerie

from valerie.navigation.models import Category
from valerie.pages.models import Type
from valerie.photos_gallery import views
from valerie.events import views
from valerie.press import views

logger = logging.getLogger(__name__)


def home(request):
    try:
        cat = Category.objects.get(slug='accueil')  # TODO AR : config ?
    except Category.DoesNotExist:
        return None

    return display_page(request, cat.get_default_page())


def display_page(request, page):
    if page.type == Type.CONTENT:
        cat = page.parent.parent
        template_path = ""

        if cat is not None:
            template_path = cat.slug + "/"

        template_path += page.slug()

        logger.debug("Display the page %s ")
        return render(request, 'pages/content/' + template_path + '.html',
                      {
                          'categories': Category.objects.filter(parent=None),
                          'current_cat': cat,
                          'page': page
                      })

    elif page.type == Type.PHOTO:
        return valerie.photos_gallery.views.display_photo(request, page.id)

    elif page.type == Type.EVENT:
        return valerie.events.views.display_event(request, page.id)

    elif page.type == Type.PRESS:
        return valerie.press.views.display_articles(request, page.id)

    else:
        logger.debug("The type of page is unknown %d", page.type)
        return None
