# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from reports.views import ReportViewSet

report_router = routers.SimpleRouter()
report_router.register('reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(report_router.urls)),
]
