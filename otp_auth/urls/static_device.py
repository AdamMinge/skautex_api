# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from otp_auth.views import StaticDeviceView

router = routers.SimpleRouter()
router.register('', StaticDeviceView, basename='static_device')

urlpatterns = [
    path('otp/static/', include(router.urls)),
]
