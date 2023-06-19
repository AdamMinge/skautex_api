# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from booking.views import BookingBlacklistViewSet

booking_blacklist_router = routers.SimpleRouter()
booking_blacklist_router.register('blacklist', BookingBlacklistViewSet, basename='booking_blacklist')

urlpatterns = [
    path('', include(booking_blacklist_router.urls)),
]
