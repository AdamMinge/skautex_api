# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from reports.models import PlayerReport
from reports.serializers import PlayerReportSerializer
from reports.policies import PlayerReportAccessPolicy
from reports.filters import PlayerReportFilter


class PlayerReportViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    permission_classes = (PlayerReportAccessPolicy,)
    serializer_class = PlayerReportSerializer
    filter_class = PlayerReportFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=PlayerReport)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, PlayerReport.objects.all()
        )
