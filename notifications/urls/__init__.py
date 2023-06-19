# Django import
from django.urls import path, include


urlpatterns = [
    path('notifications/', include('notifications.urls.fcm')),
    path('notifications/', include('notifications.urls.player_recommendation')),
]

__all__ = ['urlpatterns']
