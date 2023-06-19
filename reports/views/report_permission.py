# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from reports.models import ReportPermission
from reports.serializers import ReportPermissionSerializer
from reports.policies import ReportPermissionAccessPolicy
from reports.filters import ReportPermissionFilter


class ReportPermissionViewSet(mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):

    permission_classes = (ReportPermissionAccessPolicy,)
    serializer_class = ReportPermissionSerializer
    filter_class = ReportPermissionFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=ReportPermission)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, ReportPermission.objects.filter(report=self.kwargs['report_id'])
        )
