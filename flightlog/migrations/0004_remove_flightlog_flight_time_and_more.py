# Generated by Django 5.2 on 2025-05-12 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flightlog', '0003_flightlog_flight_level_flightlog_flight_miles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightlog',
            name='flight_time',
        ),
        migrations.RemoveField(
            model_name='flightlog',
            name='flight_type',
        ),
    ]
