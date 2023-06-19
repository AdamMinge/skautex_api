# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from cost_recording.views import UserCostRecordingViewSet
from accounts.urls.user import user_router

user_cost_recording_router = NestedSimpleRouter(user_router, 'users', lookup='user')
user_cost_recording_router.register('cost_recording', UserCostRecordingViewSet, basename='user_cost_recording')

urlpatterns = [
    path('', include(user_cost_recording_router.urls)),
]
