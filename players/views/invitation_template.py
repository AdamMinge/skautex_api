# Django import
from django.http import FileResponse
# Third-Party import
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from players.models import InvitationTemplate
from players.serializers import InvitationTemplateSerializer
from players.policies import InvitationTemplateAccessPolicy
from players.filters import InvitationTemplateFilter


class InvitationTemplateViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):

    parser_classes = (MultiPartParser,)
    permission_classes = (InvitationTemplateAccessPolicy,)
    serializer_class = InvitationTemplateSerializer
    filter_class = InvitationTemplateFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=InvitationTemplate)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, InvitationTemplate.objects.all()
        )

    @action(methods=['get'], detail=True)
    def download(self, *args, **kwargs):
        instance = self.get_object()
        file_handle = instance.template.open()

        response = FileResponse(file_handle, content_type='application/msword')
        response['Content-Length'] = instance.template.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.template.name

        return response
