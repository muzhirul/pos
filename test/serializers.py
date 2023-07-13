from rest_framework import serializers
from test.models import *

class DetailsReservationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    class Meta:
        model = DetailsReservation
        fields = '__all__'



class ReservationSerializer(serializers.ModelSerializer):
    reservation_details = DetailsReservationSerializer(many=True)
    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('reservation_details') #grab the data on details
        reservation = Reservation.objects.create(**validated_data) # create the master reservation object
        for reservation_detail in details_data:
            # create a details_reservation referencing the master reservation
            DetailsReservation.objects.create(**reservation_detail, reservation=reservation)
        return reservation