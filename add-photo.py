#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

photo = Photo(title='En Catimini', content='Verre soufflé. Rose à l\'or, 2016, 13.5cm de ht × 29ø', slug='en-catimini', position=0)
photo.photo_img.save('en-catimini.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1480498564_en-catimini.jpg', 'r')))
photo.save()

photo = Photo(title='La vie du corps', content='Verre soufflé, sablé. 2016, 32 cm de ht x 25 ø', slug='la-vie-du-corps', position=0)
photo.photo_img.save('la-vie-du-corps.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1480498617_la-vie-du-corps.jpg', 'r')))
photo.save()

photo = Photo(title='Nuages', content='Pièces en verre soufflé, découpe au sablage, 12.2016.', slug='nuages', position=0)
photo.photo_img.save('nuages.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1484815598_nuages.jpg', 'r')))
photo.save()

photo = Photo(title='En Catimini', content='Verre soufflé. Rose à l\'or, 2016, 13.5cm de ht × 29ø', slug='en-catimini', position=0)
photo.photo_img.save('1480498564_en-catimini.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload1480498564_en-catimini.jpg', 'r')))
photo.save()

photo = Photo(title='Framboise', content='Verre soufflé, découpe au sablage, satiné partiellement, liseré de lumière, 27,5x 27,5 cm, Photo Luca Delachaux', slug='framboise', position=0)
photo.photo_img.save('framboise.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1375188957_framboise.jpg', 'r')))
photo.save()

photo = Photo(title='Murmure', content='Verre soufflé, sablé, 37 cm de diam. 2012, Photo C. Lehmann', slug='murmure', position=0)
photo.photo_img.save('murmure.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1359139315_murmure.jpg', 'r')))
photo.save()

photo = Photo(title='Transparence', content='Pièce en verre soufflé, sablé. Concours FIMA 2010. Photo C. Lehmann', slug='transparence', position=0)
photo.photo_img.save('transparence.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1359131997_transparence.jpg', 'r')))
photo.save()

photo = Photo(title='Vase épis', content='Verre soufflé, découpe au sablage, poli. Photo B. Grivel', slug='vase-epis', position=0)
photo.photo_img.save('vase-epis.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1375189163_vase-epis.jpg', 'r')))
photo.save()

photo = Photo(title='Ecoute', content='Verre soufflé, découpe au sablage, photo C. Lehmann', slug='ecoute', position=0)
photo.photo_img.save('ecoute.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1375189008_ecoute.jpg', 'r')))
photo.save()

photo = Photo(title='Dans la tête', content='Verre soufflé, découpe au sablage. Photo C. Lehmann', slug='dans-la-tete', position=0)
photo.photo_img.save('dans-la-tete.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1359134260_dans-la-tete.jpg', 'r')))
photo.save()

photo = Photo(title='Elan', content='Verre soufflé, overlay de couleurs, découpe au sablage.', slug='elan', position=0)
photo.photo_img.save('elan.jpg',
        File(open('/home/aroquemaurel/projets/python/Valerie/upload/1359139347_elan.jpg', 'r')))
photo.save()

