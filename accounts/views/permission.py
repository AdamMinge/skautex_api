# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from accounts.utils import get_all_permissions
from accounts.serializers import PermissionSerializer
from accounts.policies import PermissionAccessPolicy
from accounts.filters import PermissionFilter


class PermissionViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    permission_classes = (PermissionAccessPolicy,)
    serializer_class = PermissionSerializer
    filter_class = PermissionFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, get_all_permissions()
        )
