# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
    return valerie.pages.views.display_category(request, cat)


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
        cat = Category.objects.get(slug=slug_cat)
    except Category.DoesNotExist:
        cat = None
       # TODO AR : 404

    try:
        subcat = Category.objects.get(slug=slug_subcat)
    except Category.DoesNotExist:
        subcat = None
        # TODO AR : 404

    return valerie.pages.views.display_page(request, subcat.get_default_page())


#    return _display_subcategory(request, cat, subcat)
