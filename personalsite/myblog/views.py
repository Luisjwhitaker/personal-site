from django.shortcuts import render
from .models import *

# Create your views here.

def blog_home(request): 
    items = BlogPost.objects.all()
    return render(request,'myblog/bloghome.html',{'items':items})

def post_page(request,primery_key):
    post = BlogPost.objects.get(id=primery_key)
    return render(request,'myblog/postpage.html',{'post':post})
