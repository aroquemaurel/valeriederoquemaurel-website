# Generated by Django 2.2.8 on 2020-01-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20191231_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='title',
            field=models.CharField(blank=True, max_length=256, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='documentattachment',
            name='doc',
            field=models.FileField(upload_to='', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='imageattachment',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
