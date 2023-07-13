from rest_framework import serializers
from product.models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['status','created_by','last_modified_by','created_at','updated_at']

class ProductSerializer(serializers.ModelSerializer):
    product_item = ItemSerializer(many=True)
    class Meta:
        model = Product
        exclude = ['status','created_by','last_modified_by','created_at','updated_at']

class CategorySerializer(serializers.ModelSerializer):
    product_category = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        # fields = "__all__"
        exclude = ['status','created_by','last_modified_by','created_at','updated_at']

class BrandSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True, read_only=True)
    item_brand = ItemSerializer(many=True)
    class Meta:
        model = Brand
        # fields = "__all__"
        exclude = ['status','created_by','last_modified_by','created_at','updated_at']
