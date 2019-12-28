# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.conf import settings

from valerie.common.models import ImageAttachment, DocumentAttachment


class Event(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.TextField()
    description = models.TextField()
    url = models.CharField(max_length=256, null=True)

    @property
    def is_ended(self):
        return date.today() > self.end_date

    @property
    def is_now(self):
        return self.start_date <= date.today() <= self.end_date

    def __str__(self):
        return 'from ' + self.start_date.strftime('%b %d %Y %I:%M%p') + \
               ' to ' + self.end_date.strftime('%b %d %Y %I:%M%p') + \
               ' at ' + self.location

    def get_images(self):
        return self.event_attachment_image.all().order_by('position')

    def get_documents(self):
        return self.event_attachment_document.all().order_by('position')


class ImageAttachmentEvent(ImageAttachment):
    def folder_name(self):
        return "events"

    event = models.ForeignKey('events.Event', null=True, related_name='event_attachment_image',
                              on_delete=models.CASCADE)


class DocumentAttachmentEvent(DocumentAttachment):
    def folder_name(self):
        return "events"

    event = models.ForeignKey('events.Event', null=True, related_name='event_attachment_document',
                              on_delete=models.CASCADE)
