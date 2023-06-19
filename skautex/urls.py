# Django import
from django.contrib import admin
from django.urls import path, include, re_path
# Local import
from otp_auth.admin import OTPAdminSite


admin.site.__class__ = OTPAdminSite

api_urls = [
    path('', include('core.urls')),
    path('', include('otp_auth.urls')),
    path('', include('accounts.urls')),
    path('', include('players.urls')),
    path('', include('reports.urls')),
    path('', include('rankings.urls')),
    path('', include('cost_recording.urls')),
    path('', include('booking.urls')),
    path('', include('calendars.urls')),
    path('', include('notifications.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include(api_urls)),
]
