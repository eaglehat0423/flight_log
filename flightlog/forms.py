from django import forms
from .models import FlightLog

class FlightLogForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.user = self.user  # ログインユーザーを自動設定
            instance.save()
        return instance
