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
    
    def update(self, instance, validated_data):
        details_data = validated_data.pop('reservation_details')
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        keep_reservation = []
        existing_ids = [c.id for c in instance.details_data]
        for detail_data in details_data:
            if "id"  in detail_data.key():
                if DetailsReservation.objects.filter(id=detail_data['id']).exists():
                    c = DetailsReservation.objects.get(id=detail_data['id'])
                    c.quantity = detail_data.get('quantity', c.quantity)
                    c.save()
                    keep_reservation.append(c.id)
                else:
                    continue
            else:
                continue
        return instance
