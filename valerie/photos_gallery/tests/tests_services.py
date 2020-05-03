from django.test import TestCase

from valerie.common.models import Config
from valerie.navigation.models import Category
from valerie.photos_gallery.models import PhotoGallery
from valerie.photos_gallery.services import ServiceGallery


class ServicesTest(TestCase):
    _all_photos = []
    _service_photos = None
    _category = None

    def setUp(self):
        self._category = Category.objects.create(title="Category 1", slug="category-1")

        self._all_photos = []
        for i in range(10):
            self._all_photos.append(self._create_photo(i, self._category))

        self._service_photos = ServiceGallery(self._all_photos, [])

    def test_get_previous_photos_middle(self):
        previous_photos = self._service_photos.get_previous_items(self._all_photos[5])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_photos))
        self.assertEqual(self._all_photos[2], previous_photos[0])
        self.assertEqual(self._all_photos[3], previous_photos[1])
        self.assertEqual(self._all_photos[4], previous_photos[2])

    def test_get_next_photos_middle(self):
        next_photos = self._service_photos.get_next_items(self._all_photos[5])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_photos))
        self.assertEqual(self._all_photos[6], next_photos[0])
        self.assertEqual(self._all_photos[7], next_photos[1])
        self.assertEqual(self._all_photos[8], next_photos[2])

    def test_get_next_previous_photos_middle(self):
        self.test_get_previous_photos_middle()
        self.test_get_next_photos_middle()

    def test_get_previous_photos_first_photo(self):
        previous_photos = self._service_photos.get_previous_items(self._all_photos[0])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_photos))
        self.assertEqual(self._all_photos[7], previous_photos[0])
        self.assertEqual(self._all_photos[8], previous_photos[1])
        self.assertEqual(self._all_photos[9], previous_photos[2])

    def test_get_next_photos_last_photo(self):
        next_photos = self._service_photos.get_next_items(self._all_photos[9])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_photos))
        self.assertEqual(self._all_photos[0], next_photos[0])
        self.assertEqual(self._all_photos[1], next_photos[1])
        self.assertEqual(self._all_photos[2], next_photos[2])

    def test_get_next_previous_last_photo(self):
        self.test_get_next_photos_last_photo()

        previous_photos = self._service_photos.get_previous_items(self._all_photos[9])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_photos))
        self.assertEqual(self._all_photos[6], previous_photos[0])
        self.assertEqual(self._all_photos[7], previous_photos[1])
        self.assertEqual(self._all_photos[8], previous_photos[2])

    def test_get_next_previous_photos_first_photo(self):
        self.test_get_previous_photos_first_photo()
        next_photos = self._service_photos.get_next_items(self._all_photos[0])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_photos))
        self.assertEqual(self._all_photos[1], next_photos[0])
        self.assertEqual(self._all_photos[2], next_photos[1])
        self.assertEqual(self._all_photos[3], next_photos[2])

    def test_get_previous_photos_second_photo(self):
        previous_photos = self._service_photos.get_previous_items(self._all_photos[1])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(previous_photos))
        self.assertEqual(self._all_photos[8], previous_photos[0])
        self.assertEqual(self._all_photos[9], previous_photos[1])
        self.assertEqual(self._all_photos[0], previous_photos[2])

    def test_get_next_photos_almost_last_photo(self):
        next_photos = self._service_photos.get_next_items(self._all_photos[8])
        self.assertEqual(Config.NB_ELEMENTS_AROUND_PHOTO, len(next_photos))
        self.assertEqual(self._all_photos[9], next_photos[0])
        self.assertEqual(self._all_photos[0], next_photos[1])
        self.assertEqual(self._all_photos[1], next_photos[2])

    def test_get_next_photos_few_photos(self):
        self._init_few_photos()
        next_photos = self._service_photos.get_next_items(self._all_photos[1])
        self.assertEqual(1, len(next_photos))
        self.assertEqual(self._all_photos[2], next_photos[0])

    def test_get_previous_photos_few_photos(self):
        self._init_few_photos()
        previous_photos = self._service_photos.get_previous_items(self._all_photos[1])
        self.assertEqual(1, len(previous_photos))
        self.assertEqual(self._all_photos[0], previous_photos[0])

    def test_get_previous_photos_no_photos(self):
        self._all_photos = []
        self._all_photos.append(self._create_photo(1, self._category))
        previous_photos = self._service_photos.get_previous_items(None)
        self.assertEqual(0, len(previous_photos))

    def test_get_next_photos_no_photos(self):
        self._all_photos = []
        self._service_photos = ServiceGallery(self._all_photos, [])
        self._all_photos.append(self._create_photo(1, self._category))
        next_photos = self._service_photos.get_next_items(None)
        self.assertEqual(0, len(next_photos))

    def test_get_next_photos_wrong_photo(self):
        next_photos = self._service_photos.get_next_items(self._create_photo(1, self._category))
        self.assertEqual(0, len(next_photos))

    def test_get_previous_photos_wrong_photo(self):
        previous_photos = self._service_photos.get_previous_items(self._create_photo(1, self._category))
        self.assertEqual(0, len(previous_photos))

    def _init_few_photos(self):
        self._all_photos = []
        for i in range(3):
            self._all_photos.append(self._create_photo(i, self._category))

        self._service_photos = ServiceGallery(self._all_photos, [])

    def _create_photo(self, position, category):
        no_photo = len(self._all_photos) + 1

        return PhotoGallery.objects.create(title="Photo " + str(no_photo),
                                       content_Item="Ma super photo " + str(no_photo),
                                       position_Item=position,
                                       parent=category)
