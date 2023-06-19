# Django import
from django.contrib.auth import models
# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from accounts.serializers import GroupSerializer
from accounts.policies import GroupAccessPolicy
from accounts.filters import GroupFilter


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = (GroupAccessPolicy,)
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, models.Group.objects.all()
        )
