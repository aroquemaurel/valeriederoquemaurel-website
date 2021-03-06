# Generated by Django 3.0 on 2019-12-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191231_1023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentattachmentevent',
            options={'verbose_name': 'Document en pièce jointe', 'verbose_name_plural': 'Documents en pièce jointe'},
        ),
        migrations.AlterModelOptions(
            name='imageattachmentevent',
            options={'verbose_name': 'Image en pièce jointe', 'verbose_name_plural': 'Images en pièce jointe'},
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='URL (facultatif)'),
        ),
    ]
