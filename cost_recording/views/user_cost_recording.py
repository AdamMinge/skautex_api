# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from cost_recording.models import CostRecording
from cost_recording.serializers import UserCostRecordingSerializer, UserCostRecordingCreateUpdateSerializer
from cost_recording.policies import UserCostRecordingAccessPolicy
from cost_recording.filters import CostRecordingFilter
from accounts.utils import get_user_by_id


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: UserCostRecordingSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: UserCostRecordingSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: UserCostRecordingSerializer()}))
class UserCostRecordingViewSet(mixins.MultiSerializerViewSetMixin,
                               mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):

    permission_classes = (UserCostRecordingAccessPolicy,)
    serializer_class = UserCostRecordingSerializer
    response_serializer = UserCostRecordingSerializer
    serializer_action_classes = {
        'create': UserCostRecordingCreateUpdateSerializer,
        'update': UserCostRecordingCreateUpdateSerializer,
        'partial_update': UserCostRecordingCreateUpdateSerializer,
    }
    filter_class = CostRecordingFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @property
    def user(self):
        return get_user_by_id(request=self.request, user_id=self.kwargs['user_id'])

    @swagger_fake_get_queryset(model=CostRecording)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, CostRecording.objects.filter(owner=self.user)
        )
