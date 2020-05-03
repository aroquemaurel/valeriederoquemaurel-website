# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from valerie.navigation.models import Category
from valerie.photos_gallery.models import OldPhoto
from valerie.photos_gallery.services import ServicePhotos


def display_photo(request, id_photo):
    try:
        current_photo = OldPhoto.objects.get(id=id_photo)
    except OldPhoto.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    cat = current_photo.parent

    if cat.parent is not None:
        current_cat = cat.parent
    else:
        current_cat = cat

    all_photos = OldPhoto.objects.filter(parent_id=cat.id).order_by('position', 'id')
    service_photos = ServicePhotos(all_photos)

    return render(request, 'photos_gallery/display-photo.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_cat,
                      'current_subcat': cat,
                      'previous_photos': service_photos.get_previous_photos(current_photo),
                      'next_photos': service_photos.get_next_photos(current_photo),
                      'page': current_photo
                  })
