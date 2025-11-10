# dashboard/services/statistics_service.py
from django.db.models import Count, Q, F
from .country_service import get_country_code

def compute_statistics(flights):
    total = flights.count()
    delayed = flights.filter(status='Delayed').count()
    on_time = flights.filter(status='On Time').count()
    cancelled = flights.filter(status='Cancelled').count()

    punctuality = round((on_time / total) * 100, 2) if total > 0 else 0

    return {
        'total': total,
        'delayed': delayed,
        'on_time': on_time,
        'cancelled': cancelled,
        'punctuality': punctuality
    }


def performance_by_origin(flights):
    perf = flights.values('origin').annotate(
        total_origin_flights=Count('id'),
        on_time_origin=Count('id', filter=Q(status='On Time')),
        punctuality_rate=(F('on_time_origin') * 100.0 / F('total_origin_flights'))
    ).order_by('-punctuality_rate')

    for row in perf:
        row['punctuality_rate'] = round(row['punctuality_rate'], 2)
        row['origin_country'] = get_country_code(row['origin'])

    return perf
