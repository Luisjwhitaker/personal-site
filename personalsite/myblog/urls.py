from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog home'),
    path('<str:primery_key>/', views.post_page, name='post page'),
]
