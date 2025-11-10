# dashboard/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Flight
from .forms import FlightForm
from .services.filters_service import apply_flight_filters
from .services.flight_service import build_flights_list
from .services.statistics_service import compute_statistics, performance_by_origin
from .services.opensky import obtener_vuelos_latam
from .constants import AIRPORT_COUNTRY_MAP

def index(request):
    origin_filter = request.GET.get('origin')
    destination_filter = request.GET.get('destination')

    flights = Flight.objects.all()
    flights = apply_flight_filters(flights, origin_filter, destination_filter)

    stats = compute_statistics(flights)
    perf_by_origin = performance_by_origin(flights)
    flights_list = build_flights_list(flights)

    available_origins = Flight.objects.values_list('origin', flat=True).distinct().order_by('origin')
    available_destinations = Flight.objects.values_list('destination', flat=True).distinct().order_by('destination')

    context = {
        **stats,
        'flights': flights_list,
        'performance_by_origin': perf_by_origin,
        'available_origins': available_origins,
        'available_destinations': available_destinations,
        'selected_origin': origin_filter,
        'selected_destination': destination_filter,
        'AIRPORT_COUNTRY_MAP': AIRPORT_COUNTRY_MAP,
    }
    return render(request, 'dashboard/index.html', context)

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = FlightForm()
    return render(request, 'dashboard/add_flight.html', {'form': form, 'title': '➕ Agregar Nuevo Vuelo'})


def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight.delete()
    return redirect('dashboard_home')


def edit_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)

    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = FlightForm(instance=flight)

    return render(request, 'dashboard/edit_flight.html', {'form': form, 'flight': flight})

def api_vuelos_latam(request):
    vuelos = obtener_vuelos_latam()
    return JsonResponse(vuelos, safe=False)


def mapa_vuelos(request):
    return render(request, "dashboard/mapa_vuelos.html")