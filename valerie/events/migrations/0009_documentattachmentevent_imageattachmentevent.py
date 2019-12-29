# Generated by Django 2.1.11 on 2019-12-27 18:50

from django.db import migrations, models
import django.db.models.deletion

from valerie.events.models import ImageAttachmentEvent, DocumentAttachmentEvent


def copy_image_att(apps, schema_editor):
    ImageEvent = apps.get_model('events', 'ImageEvent')

    for old_img in ImageEvent.objects.all():
        new_img = ImageAttachmentEvent()
        new_img.img = old_img.img
        new_img.position = old_img.position
        new_img.event_id = old_img.event.id
        new_img.save()


def copy_document_att(apps, schema_editor):
    DocumentEvent = apps.get_model('events', 'DocumentEvent')

    for old_doc in DocumentEvent.objects.all():
        new_doc = DocumentAttachmentEvent()
        new_doc.doc = old_doc.doc
        new_doc.position = old_doc.position
        new_doc.event_id = old_doc.event.id
        new_doc.title = old_doc.title
        new_doc.save()

class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('events', '0008_event_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentAttachmentEvent',
            fields=[
                ('documentattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.DocumentAttachment')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_attachment_document', to='events.Event')),
            ],
            bases=('common.documentattachment',),
        ),
        migrations.CreateModel(
            name='ImageAttachmentEvent',
            fields=[
                ('imageattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.ImageAttachment')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_attachment_image', to='events.Event')),
            ],
            bases=('common.imageattachment',),
        ),
        migrations.RunPython(copy_image_att),
        migrations.RunPython(copy_document_att),
    ]