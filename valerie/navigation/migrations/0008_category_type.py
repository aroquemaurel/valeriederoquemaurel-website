# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_auto_20180311_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]
