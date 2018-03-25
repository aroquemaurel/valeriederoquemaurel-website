# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('navigation', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='default_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_page', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_cat', to='navigation.Category'),
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='default_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_child_subcat', to='navigation.Category'),
        ),
    ]