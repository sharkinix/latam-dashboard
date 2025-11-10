from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        # Excluye 'punctuality' porque es un valor calculado, no de entrada
        exclude = ('punctuality',)
        # Si prefieres ser explícito, usa 'fields':
        # fields = ['flight_code', 'origin', 'destination', 'departure_time', 'arrival_time', 'status']

        # Opcional: Añadir widgets para mejor usabilidad (especialmente para fechas y horas)
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }