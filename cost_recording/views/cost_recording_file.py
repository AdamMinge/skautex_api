# Django import
from django.contrib.contenttypes.models import ContentType
# Third-Party import
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from linked_files.models import LinkedFile
from cost_recording.models import CostRecording
from cost_recording.serializers import CostRecordingFileSerializer
from cost_recording.policies import CostRecordingFileAccessPolicy


class CostRecordingFileViewSet(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):

    parser_classes = (MultiPartParser,)
    permission_classes = (CostRecordingFileAccessPolicy,)
    serializer_class = CostRecordingFileSerializer
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=LinkedFile)
    def get_queryset(self):
        ct = ContentType.objects.get_for_model(CostRecording)
        return self.access_policy.scope_queryset(
            self.request, LinkedFile.objects.filter(content_type=ct, object_id=self.kwargs['cost_recording_id'])
        )
