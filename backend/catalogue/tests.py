from django.test import TestCase
from .models import Catalogue, CatalogueImage
from django.core.files.uploadedfile import SimpleUploadedFile

class CatalogueModelTestCase(TestCase):

    def setUp(self):
        # Create a sample Catalogue object
        self.catalogue = Catalogue.objects.create(
            title="Test Catalogue",
            description="Test Description",
            featured=True
        )
        # Create a sample CatalogueImage object
        self.image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        self.catalogue_image = CatalogueImage.objects.create(
            catalogue=self.catalogue,
            image=self.image,
            position=1
        )

    def test_catalogue_creation(self):
        self.assertEqual(self.catalogue.title, "Test Catalogue")
        self.assertEqual(self.catalogue.description, "Test Description")
        self.assertTrue(self.catalogue.featured)
        self.assertIsNotNone(self.catalogue.created_at)
        self.assertIsNotNone(self.catalogue.updated_at)

    def test_catalogue_image_creation(self):
        self.assertEqual(self.catalogue_image.catalogue, self.catalogue)
        self.assertEqual(self.catalogue_image.position, 1)
        self.assertIsNotNone(self.catalogue_image.created_at)
        self.assertIsNotNone(self.catalogue_image.updated_at)

    def test_catalogue_str(self):
        self.assertEqual(str(self.catalogue), "Test Catalogue")

    def test_catalogue_image_str(self):
        self.assertEqual(str(self.catalogue_image), "Test Catalogue")

    def test_has_images(self):
        self.assertTrue(self.catalogue.has_images)

    def test_get_images(self):
        images = self.catalogue.get_images
        self.assertIn(self.catalogue_image, images)

    def test_get_thumbnail(self):
        thumbnail = self.catalogue.get_thumbnail
        self.assertIn(self.catalogue_image, thumbnail)

    def test_catalogue_without_images(self):
        new_catalogue = Catalogue.objects.create(
            title="Empty Catalogue",
            description="No Images",
            featured=False
        )
        self.assertFalse(new_catalogue.has_images)
        self.assertEqual(new_catalogue.get_images.count(), 0)
        self.assertEqual(new_catalogue.get_thumbnail, "")
