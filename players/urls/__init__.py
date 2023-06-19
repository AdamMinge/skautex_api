# Django import
from django.urls import path, include


urlpatterns = [
    path('', include('players.urls.league')),
    path('', include('players.urls.team')),
    path('', include('players.urls.player')),
    path('', include('players.urls.player_contact_detail')),
    path('', include('players.urls.invitation')),
    path('', include('players.urls.invitation_template')),
]

__all__ = ['urlpatterns']
