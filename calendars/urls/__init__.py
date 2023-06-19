# Django import
from django.urls import path, include


urlpatterns = [
    path('calendars/', include('calendars.urls.events_types')),
    path('calendars/', include('calendars.urls.events')),
    path('calendars/', include('calendars.urls.events_connected_users')),
]

__all__ = ['urlpatterns']
