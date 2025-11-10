from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_home'),
    path('add-flight/', views.add_flight, name='add_flight'),
    # Usar pk para consistencia
    path('delete-flight/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('edit/<int:pk>/', views.edit_flight, name='edit_flight'),
    path("api/vuelos-latam/", views.api_vuelos_latam, name="api_vuelos_latam"),
    path("mapa-vuelos/", views.mapa_vuelos, name="mapa_vuelos"),
]