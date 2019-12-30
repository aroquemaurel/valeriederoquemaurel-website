from abc import abstractmethod

from django.db import models
from django.conf import settings


class Attachment(models.Model):
    @abstractmethod
    def folder_name(self):
        pass

    def upload_path(self):
        return settings.UPLOAD_RELATIVE_DIR + '/' + self.folder_name()

    position = models.PositiveIntegerField()
    title = models.CharField(max_length=256)


class ImageAttachment(Attachment):
    def folder_name(self):
        pass

    img = models.ImageField(upload_to=Attachment.upload_path)


class DocumentAttachment(Attachment):
    def folder_name(self):
        pass

    doc = models.FileField(upload_to=Attachment.upload_path)

