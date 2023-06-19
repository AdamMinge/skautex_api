# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from cost_recording.views import UserCostRecordingFileViewSet
from cost_recording.urls.user_cost_recording import user_cost_recording_router

user_cost_recording_file_router = NestedSimpleRouter(user_cost_recording_router, 'cost_recording', lookup='user_cost_recording')
user_cost_recording_file_router.register('files', UserCostRecordingFileViewSet, basename='user_cost_recording_file')

urlpatterns = [
    path('', include(user_cost_recording_file_router.urls)),
]
