# Generated by Django 2.1.11 on 2019-12-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_documentattachmentevent_imageattachmentevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='imageevent',
            name='event',
        ),
        migrations.DeleteModel(
            name='DocumentEvent',
        ),
        migrations.DeleteModel(
            name='ImageEvent',
        ),
    ]
