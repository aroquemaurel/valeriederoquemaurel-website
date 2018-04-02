#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo
photo = Photo(title='Grappe de bulles', content='texte', slug='grappe-de-bulles', position=0)
photo.photo_img.save('grappe-de-bulles.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/1443676703_grappe-de-bulles.jpg', 'r')))
photo.save()

