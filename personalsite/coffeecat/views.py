from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def coffee_home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'coffeecat/coffeeindex.html',context)

def coffee_cart(request):
    #cart_items =
    context = {}
    return render(request,'coffeecat/shoppingcart.html',context)
