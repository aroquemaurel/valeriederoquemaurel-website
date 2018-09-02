# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.TextField()
    description = models.TextField()
    
# Create your models here.
