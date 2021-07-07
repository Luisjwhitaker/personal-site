from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.portfolio_home, name='portfolio home'),
    path('blog/', views.blog_home, name='blog home'),
    path('<str:primery_key>/', views.post_page, name='post page'),
    path('tag/<slug:tag_slug>', views.blog_home, name='by tag page'),

    # REST FRAMEWORK URLS
    path('api/blog/', include('myblog.api.urls','blog-api')),
]
