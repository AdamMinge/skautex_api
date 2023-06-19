# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from reports.views import ReportPlayerReportViewSet
from reports.urls.report import report_router

report_player_report_router = NestedSimpleRouter(report_router, 'reports', lookup='report')
report_player_report_router.register('player_reports', ReportPlayerReportViewSet, basename='player_report')

urlpatterns = [
    path('', include(report_player_report_router.urls)),
]
