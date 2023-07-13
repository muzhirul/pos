from django.urls import path, include
from test.views import ReservationCreate



urlpatterns = [
    path('reservation/create/', ReservationCreate.as_view(), name='reservation_create'),
    # path('category/list/', CategorytList.as_view(), name='category_list'),
    # path('product/list/', ProductList.as_view(), name='product_list'),
    # path('item/list/', ItemList.as_view(), name='item_list'),
]