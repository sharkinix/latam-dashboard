from django.db import models

class Flight(models.Model):
    flight_code = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('On Time', 'On Time'),
            ('Delayed', 'Delayed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='On Time'
    )
    punctuality = models.FloatField(
    null=True,
    blank=True,
    help_text="Puntualidad promedio en %")


    def __str__(self):
        return f"{self.flight_code} ({self.origin} → {self.destination})"
