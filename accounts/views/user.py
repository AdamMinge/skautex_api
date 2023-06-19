# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from accounts.serializers import (UserSerializer, UserCreateSerializer,
                                  UserProfilePictureUploadSerializer, UserPasswordUpdateSerializer)
from accounts.policies import UserAccessPolicy
from accounts.filters import UserFilter
from accounts.models import User


@method_decorator(name='update_password', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: UserSerializer()}))
class UserViewSet(mixins.MultiSerializerViewSetMixin,
                  mixins.UploadFileModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (UserAccessPolicy,)
    serializer_class = UserSerializer
    serializer_action_classes = {
        'upload_file': UserProfilePictureUploadSerializer,
        'create': UserCreateSerializer,
        'update_password': UserPasswordUpdateSerializer
    }
    filter_class = UserFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, User.objects.all()
        )

    def get_object(self):
        if self.kwargs['id'] == 'me':
            return self.request.user
        else:
            return super().get_object()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @action(detail=True, methods=['put'], url_path='update_password')
    def update_password(self, request, *args, **kwargs):
        user_instance = self.get_object()
        update_password_serializer = self.get_serializer(user_instance, data=request.data)
        update_password_serializer.is_valid(raise_exception=True)
        update_password_serializer.save()
        response_serializer = UserSerializer(user_instance, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_200_OK)
