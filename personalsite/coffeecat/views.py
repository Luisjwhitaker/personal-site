from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def coffee_home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'coffeecat/coffeeindex.html',context)

def coffee_menu(request):
    #products = Product.objects.all()
    #context = {'products':products}
    return render(request,'coffeecat/menu.html')#,context)

def coffee_beans(request):
    return render(request,'coffeecat/beans.html')

def coffee_drinks(request):
    return render(request,'coffeecat/drinks.html')

def coffee_food(request):
    return render(request,'coffeecat/food.html')

'''def coffee_cart(request):
    cart_items = Cart.objects.all()
    context = {'cart_items':cart_items}
    return render(request,'coffeecat/shoppingcart.html',context)

def add_to_cart(request):
    item = Product.object.filter(pk=item_id)
    if item.exists():
        item.add()
        messages.info(request,'item added to cart')
    return redirect(reverse(shopping))'''
