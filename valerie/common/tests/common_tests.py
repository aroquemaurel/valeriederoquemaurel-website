from django.test import TestCase

from valerie.navigation.models import Category


class CommonCategoryModelTests(TestCase):
    _category1 = None
    _category2 = None
    _category3 = None
    _category4 = None
    _category5 = None

    def setUp(self):
        self._category1 = Category.objects.create(title="Category 1", slug="category-1")
        self._category2 = Category.objects.create(title="Category 2", slug="category-2", parent=self._category1)
        self._category3 = Category.objects.create(title="Category 3", slug="category-3", parent=self._category2)
        self._category4 = Category.objects.create(title="Category 3", slug="category-3", parent=self._category2)
        self._category5 = Category.objects.create(title="Category 3", slug="category-3", parent=self._category4)

