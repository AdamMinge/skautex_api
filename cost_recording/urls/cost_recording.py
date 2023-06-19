# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from cost_recording.views import CostRecordingViewSet

cost_recording_router = routers.SimpleRouter()
cost_recording_router.register('cost_recording', CostRecordingViewSet, basename='cost_recording')

urlpatterns = [
    path('', include(cost_recording_router.urls)),
]
