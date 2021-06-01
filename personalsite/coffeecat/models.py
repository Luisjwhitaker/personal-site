from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=None)
    product_images = models.ImageField(upload_to=None,default='blog/bamboo.jpg')
    # 'None' in 'upload_to=None' is the name of the folder in root media url where django will dynamicaly save the imported images
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    #date_added = models.DateTimeField(auto_now_add=True)
    #customer = models.ForeignKey(Customer, on_delete=models,SET_NULL, null=True)

    def get_cartitem_subtotal(self):
        return str(int(product.product_price)*int(quantity))

    def __str__(self):
        return self.product.product_name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(CartItem)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([items.product.product_price for item in self.items.all])

    def __str__(self):
        return self.items
