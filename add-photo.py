#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

photo = Photo(title='Collier cailloux', content='Verre filé, montures argent 925, perles creuses.', slug='collier-cailloux', position=0)
photo.photo_img.save('collier-cailloux.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/1-1480500134_collier-cailloux.jpg', 'r')))
photo.save()

photo = Photo(title='Collier cailloux', content='Verre filé, montures argent 925, perles creuses.', slug='collier-cailloux', position=0)
photo.photo_img.save('collier-cailloux-2.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/2-1480500117_collier-cailloux.jpg', 'r')))
photo.save()
photo = Photo(title='Boucles cailloux', content='Verre filé, montures argent 925.', slug='boucles-cailloux', position=0)
photo.photo_img.save('boucles-cailloux.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/3-1480500090_boucles-cailloux.jpg', 'r')))
photo.save()

photo = Photo(title='Douceurs', content='Colliers sablés, verre filé, montures argent 925. Photo Baptiste Grivel.', slug='douceurs', position=0)
photo.photo_img.save('douceurs.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/4-1383063554_douceurs.jpg', 'r')))
photo.save()
photo = Photo(title='Douceurs', content='Colliers sablés, verre filé, montures argent 925. Détail. Photo Baptiste Grivel.', slug='douceurs', position=0)
photo.photo_img.save('douceurs-2.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/5-1383063586_douceurs.jpg', 'r')))
photo.save()
photo = Photo(title='Douceurs', content='Colliers sablés, verre filé, montures argent 925. Photo Baptiste Grivel.', slug='douceurs', position=0)
photo.photo_img.save('douceurs-3.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/6-1383063752_douceurs.jpg', 'r')))
photo.save()
photo = Photo(title='Collier douceurs', content='Perles creuses, verre dépoli, montures argent 925, photo B. Grivel.', slug='collier-douceurs', position=0)
photo.photo_img.save('collier-douceurs.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/7-1409665128_collier-douceurs.jpg', 'r')))
photo.save()
photo = Photo(title='Boucles bulles Douceurs', content='Perles creuses, verre dépoli, montures argent 925, photo B. Grivel.', slug='boucles-bulles-douceurs', position=0)
photo.photo_img.save('boucles-bulles-douceurs.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/8-1409665157_boucles-bulles-douceurs.jpg', 'r')))
photo.save()
photo = Photo(title='Boucles bulles filigranées', content='Perles creuses, verre filigrané, montures argent 925, photo B. Grivel.', slug='boucles-bulles-filigranees', position=0)
photo.photo_img.save('boucles-bulles-filigranees.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/9-1409665232_boucles-bulles-filigranees.jpg', 'r')))
photo.save()
photo = Photo(title='Boucles grappe de bulles', content='Perles creuses, montures argent 925, photo B. Grivel.', slug='boucles-grappe-bulles', position=0)
photo.photo_img.save('boucles-grappe-bulles.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/tmp/10-1409665261_boucles-grappes-de-bulles.jpg', 'r')))
photo.save()
