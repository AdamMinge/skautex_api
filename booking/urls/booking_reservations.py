# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from booking.views import BookingReservationsViewSet

booking_reservations_router = routers.SimpleRouter()
booking_reservations_router.register('reservations', BookingReservationsViewSet, basename='booking_reservations')

urlpatterns = [
    path('', include(booking_reservations_router.urls)),
]
