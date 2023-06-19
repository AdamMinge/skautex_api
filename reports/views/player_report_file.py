# Django import
from django.contrib.contenttypes.models import ContentType
# Third-Party import
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from linked_files.models import LinkedFile
from reports.models import PlayerReport
from reports.serializers import PlayerReportFileSerializer
from reports.policies import PlayerReportFileAccessPolicy


class PlayerReportFileViewSet(mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):

    parser_classes = (MultiPartParser,)
    permission_classes = (PlayerReportFileAccessPolicy,)
    serializer_class = PlayerReportFileSerializer
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=LinkedFile)
    def get_queryset(self):
        ct = ContentType.objects.get_for_model(PlayerReport)
        return self.access_policy.scope_queryset(
            self.request, LinkedFile.objects.filter(content_type=ct, object_id=self.kwargs['player_report_id'])
        )
