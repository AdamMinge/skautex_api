# Django import
from django.urls import path
# Local import
from otp_auth.views import JWTObtainView, JWTRefreshView

urlpatterns = [
    path('jwt/', JWTObtainView.as_view(), name='jwt'),
    path('jwt/refresh/', JWTRefreshView.as_view(), name='jwt_refresh'),
]