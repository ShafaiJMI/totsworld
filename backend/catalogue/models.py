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

class CatalogueImage(models.Model):
    catalogue = models.ForeignKey("Catalogue",on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rename_image,null=False)
    position = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)