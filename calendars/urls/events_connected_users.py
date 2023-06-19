# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from calendars.views import EventsConnectedUsersViewSet
from calendars.urls.events import events_router

events_connected_users_router = NestedSimpleRouter(events_router, 'events', lookup='event')
events_connected_users_router.register('connected_users', EventsConnectedUsersViewSet, basename='connected_users')

urlpatterns = [
    path('', include(events_connected_users_router.urls)),
]
