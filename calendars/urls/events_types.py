# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from calendars.views import EventsTypesViewSet

events_types_router = routers.SimpleRouter()
events_types_router.register('events_types', EventsTypesViewSet, basename='events_types')

urlpatterns = [
    path('', include(events_types_router.urls)),
]
