# Django import
from django.utils.decorators import method_decorator
from django.http import FileResponse
# Third-Party import
from rest_framework import viewsets, status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from players.models import Invitation
from players.serializers import InvitationCreateSerializer, InvitationGetSerializer
from players.policies import InvitationAccessPolicy
from players.filters import InvitationFilter


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: InvitationGetSerializer()}))
class InvitationViewSet(mixins.MultiSerializerViewSetMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    permission_classes = (InvitationAccessPolicy,)
    serializer_class = InvitationGetSerializer
    response_serializer = InvitationGetSerializer
    serializer_action_classes = {
        'create': InvitationCreateSerializer,
    }
    filter_class = InvitationFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=Invitation)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Invitation.objects.all()
        )

    @action(methods=['get'], detail=True)
    def download(self, *args, **kwargs):
        instance = self.get_object()
        file_handle = instance.invitation_file.open()

        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.invitation_file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.invitation_file.name
        return response
