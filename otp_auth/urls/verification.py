# Django import
from django.urls import re_path
# Local import
from otp_auth.views import DeviceVerifyView


urlpatterns = [
    re_path(r'^otp/verify/(?P<token>([0-9]{6})|([0-9]{8})|([a-z2-9]{7,8}))/$',
            DeviceVerifyView.as_view(), name='device_verify'),
]
