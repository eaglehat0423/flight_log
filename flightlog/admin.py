from django.contrib import admin

# Register your models here.

from .models import FlightLog

admin.site.register(FlightLog)