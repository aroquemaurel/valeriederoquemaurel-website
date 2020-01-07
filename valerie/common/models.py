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
    title = models.CharField(max_length=256, verbose_name="Titre", blank=True)


class ImageAttachment(Attachment):
    img = models.ImageField(verbose_name="Image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.folder_name() is not None:
            self.img.field.upload_to = self.upload_path()

    def folder_name(self):
        pass

    verbose_name = _('Image en pièce jointe')
    verbose_name_plural = _('Images en pièce jointe')


class DocumentAttachment(Attachment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.folder_name() is not None:
            self.doc.field.upload_to = self.upload_path()

    def folder_name(self):
        pass

    doc = models.FileField(verbose_name="Document")

    verbose_name = _('Document en pièce jointe')
    verbose_name_plural = _('Documents en pièce jointe')
