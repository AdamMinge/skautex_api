# Django import
from django.urls import include, path
# Third-Party import
from rest_framework_nested.routers import NestedSimpleRouter
# Local import
from otp_auth.views import OrganizationApiKeyViewSet
from otp_auth.urls.organization import organization_router

organization_api_key_router = NestedSimpleRouter(organization_router, 'organizations', lookup='organization')
organization_api_key_router.register('api_keys', OrganizationApiKeyViewSet, basename='organization_api_key')

urlpatterns = [
    path('', include(organization_api_key_router.urls)),
]
