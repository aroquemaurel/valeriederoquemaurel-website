from django.test import TestCase

from valerie.navigation.models import Category
from valerie.photos_gallery.models import PhotoGallery, VideoGallery, GalleryItem


class GalleryModelsTests(TestCase):
    _category = None

    def setUp(self):
        self._category = Category.objects.create(title="Category 1", slug="category-1")

    def test_create_photo(self):
        photo_created = PhotoGallery.objects.create(title="Photo ", parent=self._category)
        photo_expected = PhotoGallery.objects.filter(title="Photo ").first()
        self.assertEqual(photo_expected, photo_created)
        self.assertTrue(isinstance(photo_created, GalleryItem))

    def test_create_video(self):
        video_created = VideoGallery.objects.create(title="Video ", parent=self._category)
        video_expected = VideoGallery.objects.filter(title="Video ").first()
        self.assertEqual(video_expected, video_created)
        self.assertTrue(isinstance(video_created, GalleryItem))

    def test_position_default_photos(self):
        photo1 = PhotoGallery.objects.create(title="Photo 1", parent=self._category)
        photo2 = PhotoGallery.objects.create(title="Photo 2", parent=self._category)
        photo3 = PhotoGallery.objects.create(title="Photo 3", parent=self._category)
        photo4 = PhotoGallery.objects.create(title="Photo 4", parent=self._category)
        self.assertEqual(0, photo1.position_Item)
        self.assertEqual(1, photo2.position_Item)
        self.assertEqual(2, photo3.position_Item)
        self.assertEqual(3, photo4.position_Item)

    def test_position_default_videos(self):
        video1 = VideoGallery.objects.create(title="Vidéo 1", parent=self._category)
        video2 = VideoGallery.objects.create(title="Vidéo 2", parent=self._category)
        video3 = VideoGallery.objects.create(title="Vidéo 3", parent=self._category)
        video4 = VideoGallery.objects.create(title="Vidéo 4 ", parent=self._category)
        self.assertEqual(0, video1.position_Item)
        self.assertEqual(1, video2.position_Item)
        self.assertEqual(2, video3.position_Item)
        self.assertEqual(3, video4.position_Item)

    def test_position_default(self):
        item1 = PhotoGallery.objects.create(title="Photo 1", parent=self._category)
        item2 = PhotoGallery.objects.create(title="Photo 2", parent=self._category)
        item3 = VideoGallery.objects.create(title="Vidéo 1", parent=self._category)
        item4 = VideoGallery.objects.create(title="Vidéo 2", parent=self._category)
        item5 = PhotoGallery.objects.create(title="Photo 3", parent=self._category)
        item6 = PhotoGallery.objects.create(title="Photo 4", parent=self._category)
        item7 = VideoGallery.objects.create(title="Vidéo 3 ", parent=self._category)
        item8 = VideoGallery.objects.create(title="Vidéo 4", parent=self._category)

        self.assertEqual(0, item1.position_Item)
        self.assertEqual(1, item2.position_Item)
        self.assertEqual(2, item3.position_Item)
        self.assertEqual(3, item4.position_Item)
        self.assertEqual(4, item5.position_Item)
        self.assertEqual(5, item6.position_Item)
        self.assertEqual(6, item7.position_Item)
        self.assertEqual(7, item8.position_Item)
