# Django import
from django.contrib.auth import models
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from accounts.utils import get_user_by_id
from accounts.serializers import GroupSerializer, UserGroupSerializer
from accounts.policies import UserGroupAccessPolicy


class UserGroupViewSet(mixins.MultiSerializerViewSetMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    permission_classes = (UserGroupAccessPolicy,)
    serializer_class = GroupSerializer
    serializer_action_classes = {
        'list_update': UserGroupSerializer
    }
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
            self.request, self.user.groups.all()
        )

    @swagger_auto_schema(responses={status.HTTP_200_OK: GroupSerializer()})
    def list_update(self, request, *args, **kwargs):
        user_instance = self.user
        user_serializer = self.get_serializer(user_instance, data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        groups_serializer = GroupSerializer(self.paginate_queryset(self.get_queryset()), many=True, context={'request': request})
        return self.get_paginated_response(groups_serializer.data)

