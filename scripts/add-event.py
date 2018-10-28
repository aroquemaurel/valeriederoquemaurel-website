#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Add new photo
from django.core.files import File
from valerie.events.models import Event 
import datetime

event = Event(start_date=datetime.date(1930, 3, 13), end_date=datetime.date(1931, 4, 4), location='TEST', description='Super test')
event.save()

event = Event(start_date=datetime.date(2018, 3, 13), end_date=datetime.date(2019, 4, 4),
        location='BIDULE', description='Super test')
event.save()

event = Event(start_date=datetime.date(1930, 3, 13), end_date=datetime.date(1931, 4, 4),
        location='TESTOUILLE', description='Super test qui dur un petit peu')
event.save()

