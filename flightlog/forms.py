from django import forms
from .models import FlightLog

class FlightLogForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'scheduled_departure': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'scheduled_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'actual_departure': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'actual_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'takeoff_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'landing_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'total_time': forms.TimeInput(attrs={'type': 'time'}),
        }


    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
