from django.test import TestCase
from .models import Category
from .models import Image
from django.utils import timezone

# Create your tests here.
class ModelCategotyTests(TestCase):
    def setUp(self) -> None:
        Category.objects.create(
            name='TestCategory1',
        )

    def test_category_name_exist(self):
        category = Category.objects.get(name='TestCategory1')
        self.assertTrue(category is not None)

    def test_category_name_not_exist(self):
        category = Category.objects.get(name='TestCategory2')
        self.assertTrue(category is None)

class ModelImageTests(TestCase):
    def setUp(self) -> None:
        Image.objects.create(
            name='TestImage1',
            categories=Category.objects.get(name='TestCategory1'),
            created_date=timezone.now().date(),
            age_limit=12
        )

    def test_category_name_exist(self):
        image = Category.objects.get(name='TestImage1')
        self.assertTrue(image is not None)

    def test_category_name_not_exist(self):
        image = Category.objects.get(name='TestImage2')
        self.assertTrue(image is None)
