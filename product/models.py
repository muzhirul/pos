from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from supplier.models import *

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Brand Name",db_index=True)
    slug = models.SlugField(max_length=255,verbose_name="Brand Slug")
    description = models.TextField(null=True)
    status = models.BooleanField(default=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='brand_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='brand_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brand'
        verbose_name = '1. Brand'
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True, related_name='category')
    name = models.CharField(max_length=255, verbose_name="Category Name",db_index=True)
    slug = models.SlugField(max_length=255,verbose_name="Category Slug")
    description = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='category_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='category_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = '2. Category'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product_category')
    name = models.CharField(max_length=255, verbose_name="Product Name")
    slug = models.SlugField(max_length=255, verbose_name="Product Slug")
    description = models.TextField(verbose_name='Product Description')
    type = models.CharField(max_length=20, verbose_name='Product Type', null=True)
    status = models.BooleanField(default=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='product_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='product_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = '3. Product'

    def __str__(self):
        return self.name


    
class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='item_brand')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True,blank=True, related_name='supplier_item')
    name = models.CharField(max_length=255,verbose_name='Item Name')
    slug = models.SlugField(max_length=255, verbose_name="Item Slug")
    image = models.ImageField(null=True,blank=True,upload_to='items/',verbose_name='Item Image')
    size = models.CharField(max_length=255,null=True,blank=True)
    sku = models.CharField(max_length=100,null=True,blank=True,db_index=True,verbose_name='Product SKU')
    mrp = models.IntegerField(blank=True,null=True)
    discount = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True,null=True)
    status = models.BooleanField(default=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='item_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='item_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item'
        ordering = ['-created_by']
        verbose_name = '4. Item'

    def __str__(self):
        return self.product.name
    
    def delete(self):
        self.image.delete()
        super().delete()