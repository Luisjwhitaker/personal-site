from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='portfolio home'),
    path('blog/', views.blog_home, name='blog home'),
    path('<str:primery_key>/', views.post_page, name='post page'),
]
