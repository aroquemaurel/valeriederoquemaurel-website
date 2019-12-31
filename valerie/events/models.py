# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from valerie.common.models import ImageAttachment, DocumentAttachment


class Event(models.Model):
    title = models.CharField(max_length=256, verbose_name="Titre")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin")
    location = models.CharField(verbose_name="Lieu", max_length=256)
    description = models.TextField(verbose_name="Description")
    url = models.CharField(max_length=256, null=True, verbose_name="URL (facultatif)")

    @property
    def is_ended(self):
        return date.today() > self.end_date

    @property
    def is_now(self):
        return self.start_date <= date.today() <= self.end_date

    def get_images(self):
        return self.event_attachment_image.all().order_by('position')

    def get_documents(self):
        return self.event_attachment_document.all().order_by('position')

    def get_label(self):
        str_return = ""

        if self.is_ended:
            str_return = 'Terminé'
        elif self.is_now:
            str_return = 'Actuellement'
        else:
            str_return = 'Prochainement'

        return str_return

    def __str__(self):
        str_return = '['+self.get_label().upper() + '] '

        if self.title != "":
            str_return += self.title + ' '

        str_return += ' du ' + self.start_date.strftime('%d %b %Y') + \
                      ' au ' + self.end_date.strftime('%d %b %Y') + \
                      ' à ' + self.location

        return str_return

    class Meta:
        verbose_name = _('Événement')
        verbose_name_plural = _(verbose_name + 's')


class ImageAttachmentEvent(ImageAttachment):
    def folder_name(self):
        return "events"

    event = models.ForeignKey('events.Event', null=True, related_name='event_attachment_image',
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _(ImageAttachment.verbose_name)
        verbose_name_plural = _(ImageAttachment.verbose_name_plural)


class DocumentAttachmentEvent(DocumentAttachment):
    def folder_name(self):
        return "events"

    event = models.ForeignKey('events.Event', null=True, related_name='event_attachment_document',
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = _(DocumentAttachment.verbose_name)
        verbose_name_plural = _(DocumentAttachment.verbose_name_plural)
