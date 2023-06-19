# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from players.views import PlayerContactDetailViewSet
from players.urls.player import player_router

player_contact_detail_router = NestedSimpleRouter(player_router, 'players', lookup='player')
player_contact_detail_router.register('contact_details', PlayerContactDetailViewSet, basename='player_contact_detail')

urlpatterns = [
    path('', include(player_contact_detail_router.urls)),
]
