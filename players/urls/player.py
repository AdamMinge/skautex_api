# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from players.views import PlayerViewSet

player_router = routers.SimpleRouter()
player_router.register('players', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(player_router.urls)),
]
