# Generated by Django 2.2.8 on 2020-01-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos_gallery', '0003_auto_20180902_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
