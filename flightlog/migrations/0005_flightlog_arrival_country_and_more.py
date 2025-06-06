# Generated by Django 5.2 on 2025-05-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightlog', '0004_remove_flightlog_flight_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightlog',
            name='arrival_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='flightlog',
            name='departure_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='flightlog',
            name='arrival',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flightlog',
            name='departure',
            field=models.CharField(max_length=100),
        ),
    ]
