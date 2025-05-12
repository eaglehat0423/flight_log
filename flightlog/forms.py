from django import forms
from .models import FlightLog

class FlightLogForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'scheduled_departure': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'scheduled_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'actual_departure': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'actual_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'takeoff_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'landing_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'total_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }


    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
