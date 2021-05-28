from django.shortcuts import render

from django.core.paginator import Paginator
# Create your views here.

def coffee_home(request):
    return render(request,'coffeecat/coffeeindex.html')
