# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-02 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos_gallery', '0002_photo_photo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_img',
            field=models.ImageField(upload_to='upload/photos'),
        ),
    ]