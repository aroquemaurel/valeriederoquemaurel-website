from django.test import TestCase

from valerie.common.models import Config
from valerie.navigation.models import Category
from valerie.photos_gallery.models import PhotoGallery, VideoGallery
from valerie.photos_gallery.services import ServiceGallery


class ServicesTest(TestCase):
    _all_items = []
    _service_gallery = None
    _category = None

    def setUp(self):
        self._category = Category.objects.create(title="Category 1", slug="category-1")

        all_gallery_items = []
        all_videos = []
        for i in range(10):
            if i % 3 == 0:
                all_videos.append(self._create_video(i, self._category))
            else:
                all_gallery_items.append(self._create_gallery_item(i, self._category))

        self._service_gallery = ServiceGallery(all_gallery_items, all_videos)
        self._all_items = self._service_gallery._all_items

    def test_get_previous_items_middle(self):
        previous_items = self._service_gallery.get_previous_items(self._all_items[5])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_items))
        self.assertTrue(isinstance(self._all_items[5], PhotoGallery))
        self.assertEqual(self._all_items[2], previous_items[0])
        self.assertEqual(self._all_items[3], previous_items[1])
        self.assertEqual(self._all_items[4], previous_items[2])

    def test_get_next_items_middle(self):
        next_items = self._service_gallery.get_next_items(self._all_items[5])
        self.assertTrue(isinstance(self._all_items[5], PhotoGallery))
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_items))
        self.assertEqual(self._all_items[6], next_items[0])
        self.assertEqual(self._all_items[7], next_items[1])
        self.assertEqual(self._all_items[8], next_items[2])
        
    def test_get_next_previous_items_middle(self):
        self.test_get_previous_items_middle()
        self.test_get_next_items_middle()

    def test_get_previous_items_first_gallery_item(self):
        previous_items = self._service_gallery.get_previous_items(self._all_items[0])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_VIDEO, len(previous_items))
        self.assertTrue(isinstance(self._all_items[0], VideoGallery))
        self.assertEqual(self._all_items[8], previous_items[0])
        self.assertEqual(self._all_items[9], previous_items[1])

    def test_get_next_items_last_item(self):
        next_items = self._service_gallery.get_next_items(self._all_items[9])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_VIDEO, len(next_items))
        self.assertTrue(isinstance(self._all_items[9], VideoGallery))
        self.assertEqual(self._all_items[0], next_items[0])
        self.assertEqual(self._all_items[1], next_items[1])

    def test_get_next_previous_last_gallery_item(self):
        self.test_get_next_items_last_item()

        previous_items = self._service_gallery.get_previous_items(self._all_items[9])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_VIDEO, len(previous_items))
        self.assertTrue(isinstance(self._all_items[9], VideoGallery))
        self.assertEqual(self._all_items[7], previous_items[0])
        self.assertEqual(self._all_items[8], previous_items[1])

    def test_get_next_previous_items_first_gallery_item(self):
        self.test_get_previous_items_first_gallery_item()
        next_items = self._service_gallery.get_next_items(self._all_items[0])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_VIDEO, len(next_items))
        self.assertTrue(isinstance(self._all_items[0], VideoGallery))
        self.assertEqual(self._all_items[1], next_items[0])
        self.assertEqual(self._all_items[2], next_items[1])

    def test_get_previous_items_second_gallery_item(self):
        previous_items = self._service_gallery.get_previous_items(self._all_items[1])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_items))
        self.assertTrue(isinstance(self._all_items[1], PhotoGallery))
        self.assertEqual(self._all_items[8], previous_items[0])
        self.assertEqual(self._all_items[9], previous_items[1])
        self.assertEqual(self._all_items[0], previous_items[2])

    def test_get_next_items_almost_last_gallery_item(self):
        next_items = self._service_gallery.get_next_items(self._all_items[8])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_items))
        self.assertTrue(isinstance(self._all_items[8], PhotoGallery))
        self.assertEqual(self._all_items[9], next_items[0])
        self.assertEqual(self._all_items[0], next_items[1])
        self.assertEqual(self._all_items[1], next_items[2])

    def test_get_next_items_few_gallery_items(self):
        self._init_few_gallery_items()
        next_items = self._service_gallery.get_next_items(self._all_items[1])
        self.assertTrue(isinstance(self._all_items[1], PhotoGallery))
        self.assertEqual(1, len(next_items))
        self.assertEqual(self._all_items[2], next_items[0])

    def test_get_previous_items_few_gallery_items(self):
        self._init_few_gallery_items()
        previous_items = self._service_gallery.get_previous_items(self._all_items[1])
        self.assertTrue(isinstance(self._all_items[1], PhotoGallery))
        self.assertEqual(1, len(previous_items))
        self.assertEqual(self._all_items[0], previous_items[0])

    def test_get_previous_items_no_gallery_items(self):
        self._all_items = []
        self._all_items.append(self._create_gallery_item(1, self._category))
        previous_items = self._service_gallery.get_previous_items(None)
        self.assertEqual(0, len(previous_items))

    def test_get_next_items_no_gallery_items(self):
        self._all_items = []
        self._service_gallery = ServiceGallery(self._all_items, [])
        self._all_items.append(self._create_gallery_item(1, self._category))
        next_items = self._service_gallery.get_next_items(None)
        self.assertEqual(0, len(next_items))

    def test_get_next_items_wrong_gallery_item(self):
        next_items = self._service_gallery.get_next_items(self._create_gallery_item(1, self._category))
        self.assertEqual(0, len(next_items))

    def test_get_previous_items_wrong_gallery_item(self):
        previous_items = self._service_gallery.get_previous_items(self._create_gallery_item(1, self._category))
        self.assertEqual(0, len(previous_items))

    def _init_few_gallery_items(self):
        for p in self._all_items:
            p.delete()

        self._all_items = []
        for i in range(3):
            self._all_items.append(self._create_gallery_item(i, self._category))

        self._service_gallery = ServiceGallery(self._all_items, [])

    def _create_gallery_item(self, position, category):
        no_gallery_item = len(self._all_items) + 1

        return PhotoGallery.objects.create(title="Photo " + str(no_gallery_item),
                                           content_Item="Ma super photo " + str(no_gallery_item),
                                           position_Item=position,
                                           parent=category)

    def _create_video(self, position, category):
        no_video = len(self._all_items) + 1

        return VideoGallery.objects.create(title="Vidéo " + str(no_video),
                                           content_Item="Ma super vidéo " + str(no_video),
                                           position_Item=position,
                                           parent=category)
