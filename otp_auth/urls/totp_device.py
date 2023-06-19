# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from otp_auth.views import TOTPDeviceView

router = routers.SimpleRouter()
router.register('', TOTPDeviceView, basename='totp_device')

urlpatterns = [
    path('otp/totp/', include(router.urls)),
]
