# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from accounts.views import UserPermissionViewSet
from accounts.urls.user import user_router

user_permission_router = NestedSimpleRouter(user_router, 'users', lookup='user')
user_permission_router.register('permissions', UserPermissionViewSet, basename='user_permission')
user_permission_router.routes[0].mapping['put'] = 'list_update'

urlpatterns = [
    path('', include(user_permission_router.urls)),
]
