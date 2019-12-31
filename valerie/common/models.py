from abc import abstractmethod

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Attachment(models.Model):
    @abstractmethod
    def folder_name(self):
        pass

    def upload_path(self):
        return settings.UPLOAD_RELATIVE_DIR + '/' + self.folder_name()

    position = models.PositiveIntegerField(verbose_name="Position")
    title = models.CharField(max_length=256, verbose_name="Titre")


class ImageAttachment(Attachment):
    def folder_name(self):
        pass

    img = models.ImageField(upload_to=Attachment.upload_path, verbose_name="Image")

    verbose_name = _('Image en pièce jointe')
    verbose_name_plural = _('Images en pièce jointe')


class DocumentAttachment(Attachment):
    def folder_name(self):
        pass

    doc = models.FileField(upload_to=Attachment.upload_path, verbose_name="Document")

    verbose_name = _('Document en pièce jointe')
    verbose_name_plural = _('Document en pièce jointe')
