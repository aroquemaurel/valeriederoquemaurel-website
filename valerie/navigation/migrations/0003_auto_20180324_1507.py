# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('navigation', '0002_auto_20180324_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentcategory',
            name='category_ptr',
        ),
        migrations.RemoveField(
            model_name='parentcategory',
            name='default_child',
        ),
        migrations.DeleteModel(
            name='ParentCategory',
        ),
    ]
