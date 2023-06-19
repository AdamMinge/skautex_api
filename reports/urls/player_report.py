# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from reports.views import PlayerReportViewSet

player_report_router = routers.SimpleRouter()
player_report_router.register('player_reports', PlayerReportViewSet, basename='player_report')

urlpatterns = [
    path('', include(player_report_router.urls)),
]
