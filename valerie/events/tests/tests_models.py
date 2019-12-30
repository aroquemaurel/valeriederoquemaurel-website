# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from freezegun import freeze_time

from django.test import TestCase

from valerie.events.models import Event, ImageAttachmentEvent, DocumentAttachmentEvent


@freeze_time("2010-01-01")
class EventModelTests(TestCase):
    def test_end_date(self):
        e = Event(end_date=date(2018, 1, 1))
        self.assertFalse(e.is_ended)

        e = Event(end_date=date(2008, 1, 1))
        self.assertTrue(e.is_ended)

        e = Event(end_date=date(2010, 1, 1))
        self.assertFalse(e.is_ended)

    def test_is_now(self):
        e = Event(start_date=date(2015, 1, 1), end_date=date(2018, 1, 1))
        self.assertFalse(e.is_now)

        e = Event(start_date=date(2000, 1, 1), end_date=date(2003, 1, 1))
        self.assertFalse(e.is_now)

        e = Event(start_date=date(2008, 1, 1), end_date=date(2011, 1, 1))
        self.assertTrue(e.is_now)

        e = Event(start_date=date(2008, 1, 1), end_date=date(2010, 1, 1))
        self.assertTrue(e.is_now)

        e = Event(start_date=date(2010, 1, 1), end_date=date(2011, 1, 1))
        self.assertTrue(e.is_now)

    def test_get_images(self):
        event1 = Event.objects.create(title="Test1", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event2 = Event.objects.create(title="Test2", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event3 = Event.objects.create(title="Test3", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event4 = Event.objects.create(title="Test3", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")

        img1 = ImageAttachmentEvent.objects.create(position=1, title="Test 1", event=event1)
        img3 = ImageAttachmentEvent.objects.create(position=3, title="Test 3", event=event1)
        img2 = ImageAttachmentEvent.objects.create(position=2, title="Test 2", event=event1)
        img5 = ImageAttachmentEvent.objects.create(position=5, title="Test 5", event=event2)
        img4 = ImageAttachmentEvent.objects.create(position=4, title="Test 4", event=event3)
        img6 = ImageAttachmentEvent.objects.create(position=6, title="Test 6", event=event3)

        self.assertEqual(3, event1.get_images().count())
        self.assertEqual(1, event2.get_images().count())
        self.assertEqual(2, event3.get_images().count())
        self.assertEqual(0, event4.get_images().count())

        self.assertEqual(img1, event1.get_images()[0])
        self.assertEqual(img2, event1.get_images()[1])
        self.assertEqual(img3, event1.get_images()[2])

        self.assertEqual(img5, event2.get_images()[0])

        self.assertEqual(img4, event3.get_images()[0])
        self.assertEqual(img6, event3.get_images()[1])

    def test_get_documents(self):
        event1 = Event.objects.create(title="Test1", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event2 = Event.objects.create(title="Test2", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event3 = Event.objects.create(title="Test3", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")
        event4 = Event.objects.create(title="Test3", start_date=date.today(), end_date=date.today(), location="Test",
                                      description="Test")

        doc1 = DocumentAttachmentEvent.objects.create(position=1, title="Test 1", event=event1)
        doc3 = DocumentAttachmentEvent.objects.create(position=3, title="Test 3", event=event1)
        doc2 = DocumentAttachmentEvent.objects.create(position=2, title="Test 2", event=event1)
        doc5 = DocumentAttachmentEvent.objects.create(position=5, title="Test 5", event=event2)
        doc4 = DocumentAttachmentEvent.objects.create(position=4, title="Test 4", event=event3)
        doc6 = DocumentAttachmentEvent.objects.create(position=6, title="Test 6", event=event3)

        self.assertEqual(3, event1.get_documents().count())
        self.assertEqual(1, event2.get_documents().count())
        self.assertEqual(2, event3.get_documents().count())
        self.assertEqual(0, event4.get_documents().count())

        self.assertEqual(doc1, event1.get_documents()[0])
        self.assertEqual(doc2, event1.get_documents()[1])
        self.assertEqual(doc3, event1.get_documents()[2])

        self.assertEqual(doc5, event2.get_documents()[0])

        self.assertEqual(doc4, event3.get_documents()[0])
        self.assertEqual(doc6, event3.get_documents()[1])


class ImageAttachmentEventModelsTests(TestCase):
    def test_folder_name(self):
        # Be careful on this modification, it is the storage folder
        self.assertEqual("events", ImageAttachmentEvent().folder_name())


class DocumentAttachmentEventModelsTests(TestCase):
    def test_folder_name(self):
        # Be careful on this modification, it is the storage folder
        self.assertEqual("events", ImageAttachmentEvent().folder_name())
