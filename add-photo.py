#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

photo = Photo(title='Paquerettes', content='', slug='paquerettes', position=0)
photo.photo_img.save('paquerettes.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/bijoux/1359132137_paquerettes.jpg', 'r')))
photo.save()

photo = Photo(title='Bijou d\'Enfance', content='Ensemble en verre et argent 925. Photo S.  Massonnet', slug='bijoux-enfance', position=0)
photo.photo_img.save('bijoux-enfance.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/bijoux/1359144452_bijou-d-enfance.jpg', 'r')))
photo.save()

photo = Photo(title='Cailloux', content='Perles pleines réalisées au chalumeau, avec feuille d\'argent en surface. ', slug='cailloux', position=0)
photo.photo_img.save('cailloux.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/bijoux/1359140830_cailloux.jpg', 'r')))
photo.save()

photo = Photo(title='Bobines transparentes', content='Collier en verre filé, montures argent 925.', slug='bobines-transparentes', position=0)
photo.photo_img.save('bobines-transparentes.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/bijoux/1359144138_bobines-transparentes.jpg', 'r')))
photo.save()

photo = Photo(title='Collier filigrane, rouge', content='Perles creuses, verre filigrané, montures argent 925, photo B. Grivel', slug='collier-filigrane-rouge', position=0)
photo.photo_img.save('collier-filigrane-rouge.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/bijoux/1409665211_collier-filigrane-rouge.jpg', 'r')))
photo.save()

