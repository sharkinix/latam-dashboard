# dashboard/services/filters_service.py
def apply_flight_filters(flights, origin_filter, destination_filter):
    if origin_filter:
        flights = flights.filter(origin=origin_filter)

    if destination_filter:
        flights = flights.filter(destination=destination_filter)

    return flights
