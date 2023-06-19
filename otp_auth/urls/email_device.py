# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from otp_auth.views import EmailDeviceView

router = routers.SimpleRouter()
router.register('', EmailDeviceView, basename='email_device')

urlpatterns = [
    path('otp/email/', include(router.urls)),
]
