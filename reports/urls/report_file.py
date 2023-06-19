# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from reports.views import ReportFileViewSet
from reports.urls.report import report_router

report_file_router = NestedSimpleRouter(report_router, 'reports', lookup='report')
report_file_router.register('files', ReportFileViewSet, basename='report_file')

urlpatterns = [
    path('', include(report_file_router.urls)),
]
