# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from reports.models import PlayerReport
from reports.serializers import (ReportPlayerReportCreateSerializer, ReportPlayerReportUpdateSerializer,
                                 ReportPlayerReportGetSerializer)
from reports.policies import PlayerReportAccessPolicy
from reports.filters import PlayerReportFilter


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: ReportPlayerReportGetSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: ReportPlayerReportGetSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: ReportPlayerReportGetSerializer()}))
class ReportPlayerReportViewSet(mixins.MultiSerializerViewSetMixin,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):

    permission_classes = (PlayerReportAccessPolicy,)
    serializer_class = ReportPlayerReportGetSerializer
    response_serializer = ReportPlayerReportGetSerializer
    serializer_action_classes = {
        'create': ReportPlayerReportCreateSerializer,
        'update': ReportPlayerReportUpdateSerializer,
        'partial_update': ReportPlayerReportUpdateSerializer
    }
    filter_class = PlayerReportFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=PlayerReport)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, PlayerReport.objects.filter(report=self.kwargs['report_id'])
        )
