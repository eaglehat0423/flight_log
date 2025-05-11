from django.db import models
from django.contrib.auth.models import User

class FlightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    departure = models.CharField(max_length=10)
    arrival = models.CharField(max_length=10)
    aircraft_type = models.CharField(max_length=50)
    aircraft_reg = models.CharField(max_length=20, blank=True)
    flight_time = models.DecimalField(max_digits=5, decimal_places=2)
    flight_type = models.CharField(max_length=10, choices=[
        ('VFR', 'VFR'),
        ('IFR', 'IFR'),
        ('TRAINING', 'Training'),
    ])
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} | {self.departure} → {self.arrival}"
