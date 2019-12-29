from django.test import TestCase

from valerie.navigation.models import Category
from valerie.pages.models import Page, Type


class PageModelsTests(TestCase):
    _category1 = None
    _category2 = None

    def setUp(self):
        self._category1 = Category.objects.create(title="Category 1", slug="category-1")
        self._category2 = Category.objects.create(title="Category 2", slug="category-2")

    def test_title(self):
        page1 = Page.objects.create(parent=self._category1)
        self.assertEquals("Category 1", page1.title())

        page2 = Page.objects.create(parent=self._category2)
        self.assertEquals("Category 2", page2.title())

    def test_slug(self):
        page1 = Page.objects.create(parent=self._category1)
        self.assertEquals("category-1", page1.slug())

        page2 = Page.objects.create(parent=self._category2)
        self.assertEquals("category-2", page2.slug())

    def test_type_default(self):
        page1 = Page.objects.create(parent=self._category1)
        self.assertEquals(Type.PHOTO, page1.type)

        page2 = Page.objects.create(parent=self._category2, type=Type.EVENT)
        self.assertEquals(Type.EVENT, page2.type)

        page3 = Page.objects.create(parent=self._category2, type=Type.PHOTO)
        self.assertEquals(Type.PHOTO, page3.type)
