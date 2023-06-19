# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from accounts.views import UserAllPermissionViewSet
from accounts.urls.user import user_router

user_all_permission_router = NestedSimpleRouter(user_router, 'users', lookup='user')
user_all_permission_router.register('all_permissions', UserAllPermissionViewSet, basename='user_all_permission')

urlpatterns = [
    path('', include(user_all_permission_router.urls)),
]
