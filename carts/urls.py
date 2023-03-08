from django.urls import path
from django.urls import path, include
from django.conf import settings
from carts import views

urlpatterns = [
    path('', views.cart, name="cart"),
]
