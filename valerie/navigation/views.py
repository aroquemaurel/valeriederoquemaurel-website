# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import valerie

from django.shortcuts import render
from valerie.pages import views

# Create your views here.
from valerie.navigation.models import Category, ParentCategory


# Route
def display_category(request, slug):
    slug_subcat = None
    cat = None

    try:
        cat = ParentCategory.objects.get(slug=slug)

        if cat.default_child is not None:
            slug_subcat = cat.default_child.slug
        else:
            slug_subcat = None
    except ParentCategory.DoesNotExist:
        slug_subcat = None

    if slug_subcat is None and cat.get_childs().count() == 0:
        return valerie.pages.views.display_page(request, cat.default_page)

    elif slug_subcat is None:
        # TODO AR : On a des enfants, mais on connait pas la page par défaut
        return None

    return display_subcategory(request, slug, slug_subcat)


#def _display_category_without_childs(request, cat):
#    # TODO AR : on devra afficher directement le contenu de la page.
#    return render(request, 'category_list.html', {'categories': ParentCategory.objects.all(),
#                                                  'current_cat': cat,
#                                                  'current_subcat': ''})


#def _display_category(request, cat):
#    if cat is not None and cat.default_child is not None:
#        subcat = cat.default_child
#    elif cat.get_childs().count() == 0:
#        return _display_category_without_childs(request, cat)
#    else:
#        subcat = None
#
#    return _display_subcategory(request, cat, subcat)


#def _display_subcategory(request, cat, subcat):
#    if subcat is None or cat is None or subcat.default_page is None:
#        # TODO AR : on balance une 404
###        pass

#    return _display_page(request, cat, subcat, subcat.default_page)

    #return render(request, 'category_list.html', {'categories': ParentCategory.objects.all(),
#                                                      'current_cat': cat,
#                                                      'current_subcat': subcat})


# Route
def display_subcategory(request, slug_cat, slug_subcat):
    try:
        cat = ParentCategory.objects.get(slug=slug_cat)
    except Category.DoesNotExist:
        cat = None
       # TODO AR : 404

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        subcat = None
        # TODO AR : 404

    return valerie.pages.views.display_page(request, subcat.default_page)


#    return _display_subcategory(request, cat, subcat)


# Route
def category_list(request):
    try:
        slug_cat = ParentCategory.objects.get(is_home=True).slug
    except Category.DoesNotExist:
        slug_cat = None

    return display_category(request, slug_cat)


def _display_page(request, cat, subcat, page):
    if page.type == Type.PHOTO:
        pass
    elif page.type == Type.CONTENT:
        pass


    return None


# Route
def display_page(request, slug_cat, slug_subcat, id_page):
    try:
        cat = ParentCategory.objects.get(slug=slug_cat)
    except Category.DoesNotExist:
        cat = None

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        subcat = None

    return _display_page(request, cat, subcat, id_page)

