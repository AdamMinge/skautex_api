# Django import
from django.urls import include, path
# Third-Party import
from rest_framework.routers import SimpleRouter
# Local import
from otp_auth.views import OrganizationViewSet

organization_router = SimpleRouter()
organization_router.register('organizations', OrganizationViewSet, basename='organization')

urlpatterns = [
    path('', include(organization_router.urls)),
]
