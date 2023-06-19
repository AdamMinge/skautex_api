# Django import
from django.urls import path, include


urlpatterns = [
    path('', include('rankings.urls.ranking')),
]

__all__ = ['urlpatterns']
