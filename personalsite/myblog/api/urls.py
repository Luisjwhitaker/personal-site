from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<str:primery_key>/', views.api_post_page, name='api post page'),
]
