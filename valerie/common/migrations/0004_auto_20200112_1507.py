# Generated by Django 2.2.8 on 2020-01-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200105_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Position'),
        ),
    ]
