from django.urls import path
from . import views

urlpatterns = [
    path("api/products/",views.ProductListAPI.as_view(),name="product-list"),
    path("api/products/add",views.AddProductAPI.as_view(),name="add-product"),
    path("products/",views.collection,name="collection"),
    path("collection/<category_slug>/",views.collection,name="products-by-category"),
    path("p/<pslug>/",views.product_detail,name="product_detail"),
    ]