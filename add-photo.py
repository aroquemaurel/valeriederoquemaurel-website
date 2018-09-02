#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

photo = Photo(title='Pichet', content='Verre soufflé, overlay de couleur, hanse et bec soufflé
        rapportés.', slug='pichet', position=0)
photo.photo_img.save('pichet.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/art-table/1359140025_pichet.jpg', 'r')))
photo.save()

photo = Photo(title='Cuquetier', content='Pâte de cristal.', slug='Cuquetier', position=0)
photo.photo_img.save('cuquetier.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/art-table/1359140109_cuquetier.jpg', 'r')))
photo.save()

photo = Photo(title='Cuquetiers', content='Pâte de verre.', slug='Cuquetiers', position=0)
photo.photo_img.save('cuquetiers.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/art-table/1359140131_cuquetiers.jpg', 'r')))
photo.save()

photo = Photo(title='Beurrier', content='Verre soufflé, contenant en deux parties. Capuchon avec
        apports rapportés, réminiscent du beurre à étaler.', slug='beurrier', position=0)
photo.photo_img.save('beurrier.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/art-table/1359140200_beurrier.jpg', 'r')))
photo.save()

photo = Photo(title='Nids à desserts', content='Verre soufflé, posés sur un talon collé à chaud.', slug='nids-a-desserts', position=0)
photo.photo_img.save('nids-a-desserts.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/backup-photos/art-table/1359140254_nids-a-desserts.jpg', 'r')))
photo.save()

