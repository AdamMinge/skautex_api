# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from cost_recording.views import CostRecordingFileViewSet
from cost_recording.urls.cost_recording import cost_recording_router

cost_recording_file_router = NestedSimpleRouter(cost_recording_router, 'cost_recording', lookup='cost_recording')
cost_recording_file_router.register('files', CostRecordingFileViewSet, basename='cost_recording_file')

urlpatterns = [
    path('', include(cost_recording_file_router.urls)),
]
