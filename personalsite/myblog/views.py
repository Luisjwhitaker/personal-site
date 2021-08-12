from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

def blog_home(request):
    items = BlogPost.objects.all()
    paginator_object = Paginator(items, 5)
    # paginator class takes list of objects and number of objects you want form the list per page and

    page_number = request.GET.get('page')
    page_obj = paginator_object.get_page(page_number)

    return render(request,'myblog/bloghome.html',{'items':items,'page_obj':page_obj})

def post_page(request,primery_key):
    post = BlogPost.objects.get(id=primery_key)
    return render(request,'myblog/postpage.html',{'post':post})

def portfolio_home(request):
    if request.method == 'POST':
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']

        send_mail(
            contact_name,         # Email Subject
            contact_message + " by: " +contact_email,      # Email Message/Body
            contact_email,        # Email 'From:'
            ['example@mail.com'] # Email 'to:'
        )
        return render(request, 'myblog/portfolio.html',{'contact_name':contact_name})

    else:
        return render(request, 'myblog/portfolio.html',{})
