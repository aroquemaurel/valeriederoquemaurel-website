#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

photo = Photo(title='Moucharabieh', content='Verre soufflé, sablé, cristaux. Photo C. Bregnard.  Prix d\'encouragement au cours du prix Jumelles 2014, 29cm de haut.', slug='moucharabieh', position=0)
photo.photo_img.save('1404994589_moucharabieh.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/1404994589_moucharabieh.jpg', 'r')))
photo.save()

