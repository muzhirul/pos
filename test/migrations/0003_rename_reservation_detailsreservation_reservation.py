# Generated by Django 4.1.6 on 2023-07-13 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_reservation_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailsreservation',
            old_name='Reservation',
            new_name='reservation',
        ),
    ]
