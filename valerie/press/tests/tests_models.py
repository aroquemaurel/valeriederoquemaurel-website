from datetime import date

from django.test import TestCase

from valerie.press.models import Article, ImageAttachmentArticle


class ArticleModelsTests(TestCase):
    def test_get_images(self):
        article1 = Article.objects.create(title="Test1", date=date.today())
        article2 = Article.objects.create(title="Test2", date=date.today())
        article3 = Article.objects.create(title="Test3", date=date.today())
        article4 = Article.objects.create(title="Test4", date=date.today())

        img1 = ImageAttachmentArticle.objects.create(position=1, title="Test 1", article=article1)
        img3 = ImageAttachmentArticle.objects.create(position=3, title="Test 3", article=article1)
        img2 = ImageAttachmentArticle.objects.create(position=2, title="Test 2", article=article1)
        img5 = ImageAttachmentArticle.objects.create(position=5, title="Test 5", article=article2)
        img4 = ImageAttachmentArticle.objects.create(position=4, title="Test 4", article=article3)
        img6 = ImageAttachmentArticle.objects.create(position=6, title="Test 6", article=article3)

        self.assertEqual(3, article1.get_images().count())
        self.assertEqual(1, article2.get_images().count())
        self.assertEqual(2, article3.get_images().count())
        self.assertEqual(0, article4.get_images().count())

        self.assertEqual(img1, article1.get_images()[0])
        self.assertEqual(img2, article1.get_images()[1])
        self.assertEqual(img3, article1.get_images()[2])

        self.assertEqual(img5, article2.get_images()[0])

        self.assertEqual(img4, article3.get_images()[0])
        self.assertEqual(img6, article3.get_images()[1])


class ImageAttachmentArticleModelsTests(TestCase):
    def test_folder_name(self):
        # Be careful on this modification, it is the storage folder
        self.assertEqual("presse", ImageAttachmentArticle().folder_name())

