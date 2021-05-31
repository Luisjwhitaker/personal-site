from django.urls import path
from . import views

urlpatterns = [
    path('',views.coffee_home,name='coffee home'),
    path('cart/',views.coffee_cart,name='coffee cart'),
]
