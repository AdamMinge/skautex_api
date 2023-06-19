# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from reports.views import ReportPermissionViewSet
from reports.urls.report import report_router

player_permission_router = NestedSimpleRouter(report_router, 'reports', lookup='report')
player_permission_router.register('report_permissions', ReportPermissionViewSet, basename='report_permission')

urlpatterns = [
    path('', include(player_permission_router.urls)),
]
