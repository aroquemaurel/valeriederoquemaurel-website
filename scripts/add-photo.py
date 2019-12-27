#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.photos_gallery.models import Photo

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

photo = Photo(title='Valerie de Roquemaurel, chanfrein', content='C.Leutenegge',slug='valeriederoquemaurechanfrein', position=0)
photo.photo_img.save('1A_plai_09_gesteChenfreins.jpg',
        File(open('/data/www/prod/Valerie/tmp/1A_plai_09_gesteChenfreins.jpg', 'r')))
photo.save()
