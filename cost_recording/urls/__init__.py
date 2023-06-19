# Django import
from django.urls import path, include


urlpatterns = [
    path('', include('cost_recording.urls.cost_recording')),
    path('', include('cost_recording.urls.user_cost_recording')),
    path('', include('cost_recording.urls.cost_recording_file')),
    path('', include('cost_recording.urls.user_cost_recording_file')),
]

__all__ = ['urlpatterns']
