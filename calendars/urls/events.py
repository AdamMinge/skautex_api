# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from calendars.views import EventsViewSet

events_router = routers.SimpleRouter()
events_router.register('events', EventsViewSet, basename='events')

urlpatterns = [
    path('', include(events_router.urls)),
]
