import os
import sys
import django
import random
from datetime import datetime, timedelta 

# Añade la ruta base del proyecto al PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "latam_data_insights.settings")
django.setup()


from dashboard.models import Flight

cities = ['Santiago', 'Lima', 'Buenos Aires', 'São Paulo', 'Bogotá', 'Quito', 'Miami', 'Los Ángeles', 'Madrid', 'Nueva York']
statuses = ['On Time', 'Delayed', 'Cancelled']

Flight.objects.all().delete()  # Limpia la tabla antes de insertar

for i in range(15):
    origin, destination = random.sample(cities, 2)
    dep_time = datetime.now() + timedelta(hours=random.randint(-10, 10))
    arr_time = dep_time + timedelta(hours=random.randint(2, 12))
    punctuality = random.uniform(70, 100)
    
    Flight.objects.create(
        flight_code=f"LA{random.randint(100, 999)}",
        origin=origin,
        destination=destination,
        departure_time=dep_time,
        arrival_time=arr_time,
        status=random.choice(statuses),
        punctuality=round(punctuality, 2)
    )

print("✅ 15 vuelos de ejemplo creados correctamente.")
