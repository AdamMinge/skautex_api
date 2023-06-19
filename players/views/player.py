# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from players.models import Player
from players.serializers import PlayerSerializer, PlayerCreateUpdateSerializer, PlayerProfilePictureUploadSerializer
from players.policies import PlayerAccessPolicy
from players.filters import PlayerFilter


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: PlayerSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: PlayerSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: PlayerSerializer()}))
class PlayerViewSet(mixins.MultiSerializerViewSetMixin,
                    mixins.UploadFileModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (PlayerAccessPolicy,)
    serializer_class = PlayerSerializer
    response_serializer = PlayerSerializer
    serializer_action_classes = {
        'upload_file': PlayerProfilePictureUploadSerializer,
        'create': PlayerCreateUpdateSerializer,
        'update': PlayerCreateUpdateSerializer,
        'partial_update': PlayerCreateUpdateSerializer
    }
    filter_class = PlayerFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Player.objects.all()
        )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
