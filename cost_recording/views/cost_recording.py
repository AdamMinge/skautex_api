# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from cost_recording.models import CostRecording
from cost_recording.serializers import CostRecordingSerializer, CostRecordingCreateUpdateSerializer
from cost_recording.policies import CostRecordingAccessPolicy
from cost_recording.filters import CostRecordingFilter


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: CostRecordingSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: CostRecordingSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: CostRecordingSerializer()}))
class CostRecordingViewSet(mixins.MultiSerializerViewSetMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):

    permission_classes = (CostRecordingAccessPolicy,)
    serializer_class = CostRecordingSerializer
    response_serializer = CostRecordingSerializer
    serializer_action_classes = {
        'create': CostRecordingCreateUpdateSerializer,
        'update': CostRecordingCreateUpdateSerializer,
        'partial_update': CostRecordingCreateUpdateSerializer,
    }
    filter_class = CostRecordingFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=CostRecording)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, CostRecording.objects.all()
        )