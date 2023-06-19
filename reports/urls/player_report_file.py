# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from reports.views import PlayerReportFileViewSet
from reports.urls.report_player_report import report_player_report_router

player_report_file_router = NestedSimpleRouter(report_player_report_router, 'player_reports', lookup='player_report')
player_report_file_router.register('files', PlayerReportFileViewSet, basename='player_report_file')

urlpatterns = [
    path('', include(player_report_file_router.urls)),
]
