from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
#from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from core.models import Review
from category.models import Category
from .recent import RecentProduct
from rest_framework import status
from .serializers import ProductSerializer

# Create your views here.
class AddProductAPI(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        productserializer = ProductSerializer(data=request.data)
        if productserializer.is_valid():
            productserializer.save()

            images_data = request.FILES.getlist('images')  # Assuming 'images' is the key for image files
            for image_data in images_data:
                image_serializer = ProductImageSerializer(data={'product': product.id, 'image': image_data})
                if image_serializer.is_valid():
                    image_serializer.save()  # Save the product image instance
                else:
                    # Handle invalid image data
                    product.delete()  # Rollback creation of product if image data is invalid
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(productserializer.data, status=status.HTTP_201_CREATED)
        return Response(productserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListAPI(APIView):
    renderer_classes = [JSONRenderer]
    @csrf_exempt
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

def collection(request,category_slug=None):
    category = None
    categories= Category.objects.all()
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    context = {
            'page_title' : 'Collection',
            'categories':categories,
            'products':products,
            }
    #messages.info(request,'Site Under construction')
    return render(request,"product.html",context)

def product_detail(request,pslug):
    recent_product = RecentProduct(request)
    categories = Category.objects.all()
    product = Product.objects.get(slug=pslug)
    reviews = Review.objects.filter(product=product)
    recent_product.add(product=product)
    context = {
    'categories':categories,
    'product':product,
    'reviews':reviews,
        }
    #messages.info(request,'Site Under construction')
    return render(request,'single_product.html',context)