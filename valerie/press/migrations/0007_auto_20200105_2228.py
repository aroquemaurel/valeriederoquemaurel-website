# Generated by Django 2.2.8 on 2020-01-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0006_auto_20191227_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
