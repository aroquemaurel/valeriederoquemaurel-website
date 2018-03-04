# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from valerie.navigation.models import Category


def category(request, slug):
    text = slug
    # TODO AR : on affiche une catégorie, avec une sous-catégorie par défaut, et toutes les sous-catégories sont listées
    return HttpResponse(text)


def sub_category(request, slug_cat, slug_subcat):
    # TODO AR : on affiche une catégorie et une sous-catégorie, et toutes les sous-catégories sont listées
    return HttpResponse(slug_cat+slug_subcat)


def category_list(request):

    return render(request, 'category_list.html', {'categories': Category.objects.filter(parent=None)})