# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import models


class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.TextField()
    description = models.TextField()

    @property
    def is_ended(self):
        return date.today() > self.end_date

    @property
    def is_now(self):
        return self.start_date <= date.today() <= self.end_date

    def __str__(self):
        return 'from ' + self.start_date.strftime('%b %d %Y %I:%M%p')+\
               ' to '+self.end_date.strftime('%b %d %Y %I:%M%p')+\
               ' at '+self.location

