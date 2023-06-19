# Django import
from django.contrib.auth import models
# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from accounts.utils import get_all_permissions_for_user, get_user_by_id
from accounts.serializers import PermissionSerializer
from accounts.policies import UserAllPermissionAccessPolicy
from accounts.filters import PermissionFilter


class UserAllPermissionViewSet(mixins.ListModelMixin,
                               viewsets.GenericViewSet):

    permission_classes = (UserAllPermissionAccessPolicy,)
    serializer_class = PermissionSerializer
    filter_class = PermissionFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @property
    def user(self):
        return get_user_by_id(request=self.request, user_id=self.kwargs['user_id'])

    @swagger_fake_get_queryset(model=models.Permission)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, get_all_permissions_for_user(self.user)
        )
