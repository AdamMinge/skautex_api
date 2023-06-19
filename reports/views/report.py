# Python Import
import io
# Django import
from django.http import HttpResponse
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from reports.models import Report
from reports.serializers import ReportSerializer, ReportCreateUpdateSerializer
from reports.policies import ReportAccessPolicy
from reports.filters import ReportFilter
from reports.utils import ReportDocument


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: ReportSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: ReportSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: ReportSerializer()}))
class ReportViewSet(mixins.MultiSerializerViewSetMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (ReportAccessPolicy,)
    serializer_class = ReportSerializer
    response_serializer = ReportSerializer
    serializer_action_classes = {
        'create': ReportCreateUpdateSerializer,
        'update': ReportCreateUpdateSerializer,
        'partial_update': ReportCreateUpdateSerializer
    }
    filter_class = ReportFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=Report)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Report.objects.all()
        )

    @action(methods=['get'], detail=True)
    def download(self, *args, **kwargs):
        document = ReportDocument(self.get_object())
        file_stream = io.BytesIO()
        document.save(file_stream)
        file_stream.seek(0)
        document_value = file_stream.getvalue()

        response = HttpResponse(document_value, content_type='application/msword')
        response['Content-Length'] = len(document_value)
        response['Content-Disposition'] = f'attachment; filename="{document.name()}.docx"'
        return response
