from django.db import models
import uuid
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Reservation Name')
    user_reservation = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='reservation_creator', editable=False, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return str(self.name)

class DetailsReservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reservation = models.ForeignKey(Reservation, blank=True,null=True, on_delete=models.CASCADE,related_name='reservation_details')
    quantity = models.IntegerField(null=False, default=0, blank=False)

    class Meta:
        db_table = 'detail_reservation'

    def __str__(self):
        return str(self.reservation.name)
    