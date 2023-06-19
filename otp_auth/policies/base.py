# Third-Party import
from rest_framework.permissions import IsAuthenticated
# Local import
from core.permissions import BaseAccessPolicy
from otp_auth.permissions import HasOrganizationAPIKey
from otp_auth.permissions import Verified


class APIKeyAccessPolicy(BaseAccessPolicy):
    def __init__(self):
        self.has_organization_api_key = HasOrganizationAPIKey()

    def has_permission(self, request, view):
        return self.has_organization_api_key.has_permission(request, view) and \
               BaseAccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.has_organization_api_key.has_object_permission(request, view, obj) and \
               BaseAccessPolicy.has_object_permission(self, request, view, obj)


class AuthenticatedAccessPolicy(APIKeyAccessPolicy):
    def __init__(self):
        super().__init__()
        self.is_authenticated = IsAuthenticated()

    def has_permission(self, request, view):
        return self.is_authenticated.has_permission(request, view) and \
               APIKeyAccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.is_authenticated.has_object_permission(request, view, obj) and \
               APIKeyAccessPolicy.has_object_permission(self, request, view, obj)


class VerifiedAccessPolicy(APIKeyAccessPolicy):
    def __init__(self):
        super().__init__()
        self.verified = Verified()

    def has_permission(self, request, view):
        return self.verified.has_permission(request, view) and \
               APIKeyAccessPolicy.has_permission(self, request, view)

    def has_object_permission(self, request, view, obj):
        return self.verified.has_object_permission(request, view, obj) and \
               APIKeyAccessPolicy.has_object_permission(self, request, view, obj)

