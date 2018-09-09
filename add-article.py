#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.press.models import Article 
from valerie.press.models import ImageArticle 
import datetime

article = Article(date=datetime.date(2017, 11, 1), title="Accrochages, nov. 2017", content="",
        youtube_link=None)
article.save()
image_article = ImageArticle(position=1, article=article)
image_article.img.save('accrochages-1.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-presse/presse/171031_AccroLég.jpg', 'r')))
image_article.img.save('accrochages-2.jpg', File(open('/home/aroquemaurel/projets/python/Valerie/backup-presse/presse/171105_Accro.jpeg', 'r')))
image_article.save()

