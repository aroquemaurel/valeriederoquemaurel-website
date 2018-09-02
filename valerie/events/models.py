# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return 'from ' + self.start_date.strftime('%b %d %Y %I:%M%p')+\
               ' to '+self.end_date.strftime('%b %d %Y %I:%M%p')+\
               ' at '+self.location

