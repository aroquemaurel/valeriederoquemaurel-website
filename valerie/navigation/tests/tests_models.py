from valerie.common.tests.common_tests import CommonCategoryModelTests
from valerie.pages.models import Page


class CategoryModelTests(CommonCategoryModelTests):
    def test_get_pages(self):
        page1 = Page.objects.create(parent=self._category1)
        page2 = Page.objects.create(parent=self._category1)
        page3 = Page.objects.create(parent=self._category2)
        page4 = Page.objects.create(parent=self._category1)
        page5 = Page.objects.create(parent=self._category1)
        page6 = Page.objects.create(parent=self._category2)
        page7 = Page.objects.create(parent=self._category2)

        self.assertEqual(4, self._category1.get_pages().count())
        self.assertTrue(page1 in self._category1.get_pages())
        self.assertTrue(page2 in self._category1.get_pages())
        self.assertTrue(page4 in self._category1.get_pages())
        self.assertTrue(page5 in self._category1.get_pages())

        self.assertEqual(3, self._category2.get_pages().count())
        self.assertTrue(page3 in self._category2.get_pages())
        self.assertTrue(page6 in self._category2.get_pages())
        self.assertTrue(page7 in self._category2.get_pages())

        self.assertEqual(0, self._category3.get_pages().count())

    def test_get_default_page(self):
        page1 = Page.objects.create(parent=self._category1)
        Page.objects.create(parent=self._category2)
        Page.objects.create(parent=self._category2)
        Page.objects.create(parent=self._category2)

        self._category1.default_page = page1
        self.assertEqual(page1, self._category1.get_default_page())
        self.assertIsNone(self._category3.get_default_page())

    def test_get_childs(self):
        self.assertEqual(1, self._category1.get_childs().count())
        self.assertEqual(self._category2, self._category1.get_childs()[0])

        self.assertEqual(2, self._category2.get_childs().count())
        self.assertEqual(self._category3, self._category2.get_childs()[0])
        self.assertEqual(self._category4, self._category2.get_childs()[1])

        self.assertEqual(0, self._category5.get_childs().count())

