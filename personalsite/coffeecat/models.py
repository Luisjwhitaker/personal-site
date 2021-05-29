from django.db import models
from PIL import Image
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=None)
    product_images = models.ImageField(upload_to=None,default='blog/bamboo.jpg')

    def __str__(self):
        return self.product_name

#class ProductAttribute():
#    product=models.ForeignKey(Product,on_delete=models.CASCADE)
