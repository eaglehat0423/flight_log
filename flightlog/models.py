from django.db import models
from django.contrib.auth.models import User

class FlightLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    # 基本情報
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    aircraft_type = models.CharField(max_length=50)
    aircraft_reg = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)

    # 追加項目
    airline = models.CharField(max_length=50, blank=True)  # 航空会社
    flight_number = models.CharField(max_length=20, blank=True)  # 便名
    seat_class = models.CharField(max_length=20, blank=True)  # クラス (例: Economy)
    seat_number = models.CharField(max_length=10, blank=True)  # 座席番号

    departure_gate = models.CharField(max_length=10, blank=True)
    departure_spot = models.CharField(max_length=10, blank=True)
    arrival_gate = models.CharField(max_length=10, blank=True)
    arrival_spot = models.CharField(max_length=10, blank=True)

    scheduled_departure = models.DateTimeField(blank=True, null=True)
    scheduled_arrival = models.DateTimeField(blank=True, null=True)
    actual_departure = models.DateTimeField(blank=True, null=True)
    actual_arrival = models.DateTimeField(blank=True, null=True)
    takeoff_time = models.DateTimeField(blank=True, null=True)
    landing_time = models.DateTimeField(blank=True, null=True)

    takeoff_runway = models.CharField(max_length=10, blank=True)
    landing_runway = models.CharField(max_length=10, blank=True)

    flight_level = models.IntegerField(null=True, blank=True)
    total_time = models.DurationField(null=True, blank=True)
    flight_miles = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.date} | {self.departure} → {self.arrival}"
