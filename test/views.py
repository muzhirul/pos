from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from test.models import *
from test.serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class ReservationCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     # print(data)
    #     data["userReservation"] = request.user.id
    #     print(data)
    #     serializer = ReservationSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

class ReservationUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer