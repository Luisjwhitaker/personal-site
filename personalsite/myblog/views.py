from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def blog_home(request):
    items = BlogPost.objects.all()
    paginator = Paginator(items, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'myblog/bloghome.html',{'items':items,'page_obj':page_obj})

def post_page(request,primery_key):
    post = BlogPost.objects.get(id=primery_key)
    return render(request,'myblog/postpage.html',{'post':post})
