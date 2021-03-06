# Generated by Django 2.2.8 on 2020-05-03 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos_gallery', '0007_auto_20200503_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('galleryitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='photos_gallery.GalleryItem')),
                ('youtube_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Lien Youtube')),
            ],
            bases=('photos_gallery.galleryitem',),
        ),
    ]
