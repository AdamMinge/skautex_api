# Django import
from django.urls import path, include


urlpatterns = [
 # --------------------- hide endpoints ------------------------
 # path('', include('otp_auth.urls.organization')),
 # path('', include('otp_auth.urls.organization_api_key')),
 # -------------------------------------------------------------
    path('', include('otp_auth.urls.jwt')),
    path('', include('otp_auth.urls.totp_device')),
    path('', include('otp_auth.urls.verification')),
    path('', include('otp_auth.urls.static_device')),
    path('', include('otp_auth.urls.email_device')),
]

__all__ = ['urlpatterns']
