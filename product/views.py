from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from product.models import *
from product.serializers import *
# from rest_framework.permissions import IsAdminUser

# Create your views here.
class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BrandSerializer(queryset,many=True)
        response = {
           "message": "Brand list",
           "error": False,
           "code": 200,
           "results": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CategorytList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        if queryset:
            message = 'Category List'
            code = 200
        else:
            message = 'No Category Found'
            code = 404
        response = {
           "message": message,
           "error": False,
           "code": code,
           "results": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        if queryset:
            message = 'Product List'
            code = 200
        else:
            message = 'No Product Found'
            code = 404
        response = {
           "message": message,
           "error": False,
           "code": code,
           "results": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        if queryset:
            message = 'Item List'
            code = 200
        else:
            message = 'No Item Found'
            code = 404
        response = {
           "message": message,
           "error": False,
           "code": code,
           "results": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)