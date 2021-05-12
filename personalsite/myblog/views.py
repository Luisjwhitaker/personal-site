from django.shortcuts import render
from .models import *

# Create your views here.

def blog_home(request):
    items = BlogPost.objects.all()
    return render(request,'myblog/bloghome.html',{'items':items})
