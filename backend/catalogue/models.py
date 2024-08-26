from django.db import models
from django.shortcuts import reverse
from core.utils import rename_image

# Create your models here.
class Catalogue(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(max_length=250,blank=True,null=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    @property
    def has_images(self):
        if CatalogueImage.objects.filter(catalogue=self) != None:
            return True
        return False
    @property
    def get_images(self):
        return CatalogueImage.objects.filter(catalogue=self)
    @property
    def get_thumbnail(self):
        thumbnail_queryset = CatalogueImage.objects.filter(catalogue=self)
        if thumbnail_queryset.exists():
            return thumbnail_queryset  # Assuming 'image' is the field name containing the thumbnail URL
        else:
            return ""

class CatalogueImage(models.Model):
    catalogue = models.ForeignKey("Catalogue",on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rename_image,null=False)
    position = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)