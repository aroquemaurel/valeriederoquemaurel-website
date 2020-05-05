# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from valerie.navigation.models import Category
from valerie.photos_gallery.models import GalleryItem, PhotoGallery, VideoGallery
from valerie.photos_gallery.services import ServiceGallery

import logging

logger = logging.getLogger(__name__)


def display_photo(request, id_photo):
    try:
        current_item = PhotoGallery.objects.get(id=id_photo)
    except GalleryItem.DoesNotExist:
        try:
            logger.debug("Photo %d is not found, search video", id_photo)
            current_item = VideoGallery.objects.get(id=id_photo)
        except VideoGallery.DoesNotExist:
            logger.error("The photo or the video %d doest not exists.", id_photo)
            return HttpResponseNotFound('<h1>Page not found</h1>')

    cat = current_item.parent

    if cat.parent is not None:
        current_cat = cat.parent
    else:
        current_cat = cat

    all_photos = PhotoGallery.objects.filter(parent_id=cat.id).order_by('position_Item', 'id')
    all_videos = VideoGallery.objects.filter(parent_id=cat.id).order_by('position_Item', 'id')
    service_gallery = ServiceGallery(all_photos, all_videos)

    return render(request, 'photos_gallery/display-photo.html',
                  {
                      'categories': Category.objects.filter(parent=None),
                      'current_cat': current_cat,
                      'current_subcat': cat,
                      'previous_photos': service_gallery.get_previous_items(current_item),
                      'next_photos': service_gallery.get_next_items(current_item),
                      'page': current_item,
                      'is_photo': isinstance(current_item, PhotoGallery)
                  })
