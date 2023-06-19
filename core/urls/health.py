# Django import
from django.urls import path, include

urlpatterns = [
    path('', include('health_check.urls')),
]
