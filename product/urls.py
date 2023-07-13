from django.urls import path, include
from product.views import BrandList,CategorytList, ProductList, ItemList



urlpatterns = [
    path('brand/list/', BrandList.as_view(), name='brand_list'),
    path('category/list/', CategorytList.as_view(), name='category_list'),
    path('product/list/', ProductList.as_view(), name='product_list'),
    path('item/list/', ItemList.as_view(), name='item_list'),
]