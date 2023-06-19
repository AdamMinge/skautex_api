# Django import
from django.conf.urls import include
from django.urls import re_path
# Third-Party import
from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework.routers import DefaultRouter

fcm_router = DefaultRouter()
fcm_router.register(r'devices', FCMDeviceViewSet)


urlpatterns = [
    re_path(r'^', include(fcm_router.urls)),
]
