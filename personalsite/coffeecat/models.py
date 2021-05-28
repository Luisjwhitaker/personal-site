from django.db import models
from PIL import Image
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=None)
    product_images = models.ImageField(upload_to=None)

    def __str__(self):
        return self.title
