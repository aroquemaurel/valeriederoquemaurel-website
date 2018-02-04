# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User
    # Si besoin d'autres infos

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
