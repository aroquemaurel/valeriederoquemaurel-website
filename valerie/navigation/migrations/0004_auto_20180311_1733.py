# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0003_auto_20180311_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='default_child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_child_subcat', to='navigation.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_cat', to='navigation.Category'),
        ),
    ]
