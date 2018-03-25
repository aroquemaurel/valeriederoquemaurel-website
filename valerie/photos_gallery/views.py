# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from valerie.navigation.models import Category
from valerie.photos_gallery.models import Photo


def display_photo(request, id_photo):
    # TODO AR : afficher categorie, sous categorie, liste sous categorie et photo associé en paramètre
    try:
        photo = Photo.objects.get(id=id_photo)
    except Category.DoesNotExist:
        # TODO AR : return 404
        return None

    current_cat = photo.parent

    return render(request, 'photos_gallery/display-photo.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_cat,
                      'page': photo,
                      'all_photos': current_cat.get_pages()
                  })
