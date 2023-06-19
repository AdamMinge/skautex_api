# Django import
from django.urls import path, include


urlpatterns = [
    path('booking/', include('booking.urls.booking_objects_types')),
    path('booking/', include('booking.urls.booking_objects')),
    path('booking/', include('booking.urls.booking_blacklist')),
    path('booking/', include('booking.urls.booking_reservations')),
]

__all__ = ['urlpatterns']
