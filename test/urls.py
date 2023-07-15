from django.urls import path, include
from test.views import ReservationCreate, ReservationUpdate



urlpatterns = [
    path('reservation/create/', ReservationCreate.as_view(), name='reservation_create'),
    path('reservation/update/<pk>', ReservationUpdate.as_view(), name='reservation_update'),
    
]