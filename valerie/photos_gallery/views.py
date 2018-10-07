# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
from valerie.navigation.models import Category
from valerie.photos_gallery.models import Photo


def display_photo(request, id_photo):
    try:
        current_photo = Photo.objects.get(id=id_photo)
    except Photo.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    cat = current_photo.parent

    if cat.parent is not None:
        current_cat = cat.parent
    else:
        current_cat = cat

    all_photos = Photo.objects.filter(parent_id=cat.id).order_by('position')

    previous_photo = []
    next_photo = []
    fill_previous = True
    nb_elements_around_photo = 3
    for photo in all_photos:
        if photo.id == current_photo.id:
            fill_previous = False
        elif fill_previous:
            previous_photo.append(photo)
        else:
            next_photo.append(photo)

    if len(previous_photo) > nb_elements_around_photo:
        previous_photo = previous_photo[::-1][:nb_elements_around_photo]

    if len(next_photo) > nb_elements_around_photo:
        next_photo = next_photo[:nb_elements_around_photo]

    return render(request, 'photos_gallery/display-photo.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_cat,
                      'current_subcat': cat,
                      'previous_photos': previous_photo,
                      'next_photos': next_photo,
                      'page': current_photo
                  })
