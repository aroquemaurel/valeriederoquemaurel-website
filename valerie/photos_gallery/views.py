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
        current_photo = Photo.objects.get(id=id_photo)
    except Photo.DoesNotExist:
        # TODO AR : return 404
        return None

    cat = current_photo.parent

    if cat.parent is not None:
        current_cat = cat.parent
    else:
        current_cat = cat

    all_photos = Photo.objects.filter(parent_id=cat.id).order_by('position')

    previous_photo = []
    next_photo = []
    fill_previous = True
    nb_elements_around_photo = 2
    for photo in all_photos:
        if photo.id == current_photo.id:
            fill_previous = False
        elif fill_previous:
            previous_photo.append(photo)
        else:
            next_photo.append(photo)

    if len(previous_photo) > nb_elements_around_photo:
        previous_photo = previous_photo[nb_elements_around_photo*-1]

    if len(next_photo) > nb_elements_around_photo:
        next_photo = previous_photo[nb_elements_around_photo * -1]

    return render(request, 'photos_gallery/display-photo.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_cat,
                      'current_subcat': cat,
                      'previous_photos': previous_photo,
                      'next_photos': next_photo,
                      'page': current_photo
                  })
