# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from booking.views import BookingObjectsViewSet

booking_objects_router = routers.SimpleRouter()
booking_objects_router.register('objects', BookingObjectsViewSet, basename='booking_objects')

urlpatterns = [
    path('', include(booking_objects_router.urls)),
]
