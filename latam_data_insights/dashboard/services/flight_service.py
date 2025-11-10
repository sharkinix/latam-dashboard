# dashboard/services/flight_service.py
from ..constants import AIRPORT_COUNTRY_MAP

from ..constants import AIRPORT_COUNTRY_MAP

def build_flights_list(flights):
    flight_data = []
    for f in flights:
        origin_country = AIRPORT_COUNTRY_MAP.get(f.origin, '').lower()
        destination_country = AIRPORT_COUNTRY_MAP.get(f.destination, '').lower()

        flight_data.append({
            'id': f.id,
            'pk': f.pk,
            'flight_code': f.flight_code,
            'origin': f.origin,
            'destination': f.destination,
            'departure_time': f.departure_time,
            'arrival_time': f.arrival_time,
            'status': f.status,
            'origin_country': origin_country,
            'destination_country': destination_country,
        })
    return flight_data
