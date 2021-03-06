# Generated by Django 2.2.8 on 2020-01-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0007_auto_20200105_2228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='imageattachmentarticle',
            options={'verbose_name': 'Image en pièce jointe', 'verbose_name_plural': 'Images en pièce jointe'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(verbose_name="Date de l'article"),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='article',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Lien Youtube'),
        ),
    ]
