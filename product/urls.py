from django.urls import path, include
from product.views import BrandList,CategorytList, ProductList, ItemList
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)



urlpatterns = [
    path('brand/list/', BrandList.as_view(), name='brand_list'),
    path('category/list/', CategorytList.as_view(), name='category_list'),
    path('product/list/', ProductList.as_view(), name='product_list'),
    path('item/list/', ItemList.as_view(), name='item_list'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]