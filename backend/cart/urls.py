from django.urls import path
from . import views
from .cartapi import CartAPI

urlpatterns = [
    path("api/cart-list/",CartAPI.as_view(),name="cart-list-api"),
    path("api/add-to-cart/<int:product_pk>/",CartAPI.as_view(),name="add-to-cart"),
    path("cart/",views.cart,name="cart"),
    #path("add-to-cart/<product_slug>/",views.addtocart,name="add-to-cart"),
    path("remove-from-cart/<product_slug>/",views.removefromcart,name="remove-from-cart"),
    ]