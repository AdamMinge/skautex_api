# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from booking.views import BookingObjectsTypesViewSet

booking_objects_types_router = routers.SimpleRouter()
booking_objects_types_router.register('objects_types', BookingObjectsTypesViewSet, basename='booking_objects_types')

urlpatterns = [
    path('', include(booking_objects_types_router.urls)),
]
