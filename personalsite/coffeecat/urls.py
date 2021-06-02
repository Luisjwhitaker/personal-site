from django.urls import path
from . import views

urlpatterns = [
    path('',views.coffee_home,name='coffee home'),
    path('menu/',views.coffee_menu,name='coffee menu'),
    path('beans/',views.coffee_beans,name='coffee beans'),
    path('drinks/',views.coffee_drinks,name='coffee drinks'),
    path('food/',views.coffee_food,name='coffee food'),
    #path('cart/',views.coffee_cart,name='coffee cart'),
]
