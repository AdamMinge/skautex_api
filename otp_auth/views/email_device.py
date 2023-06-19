# Third-Party import
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django_otp.plugins.otp_email.models import EmailDevice
# Local import
from core import mixins
from otp_auth.utils import send_token_to_email_devices
from otp_auth.serializers import EmailDeviceSerializer, EmailDeviceCreateSerializer
from otp_auth.policies import EmailDeviceAccessPolicy, EmailDeviceSendTokenAccessPolicy
from otp_auth.filters import EmailDeviceFilter


class EmailDeviceView(mixins.MultiSerializerViewSetMixin,
                      mixins.MultiPermissionViewSetMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = EmailDeviceSerializer
    serializer_action_classes = {
        'create': EmailDeviceCreateSerializer
    }
    permission_classes = [EmailDeviceAccessPolicy]
    permission_action_classes = {
        'send_token_to_emails': [EmailDeviceSendTokenAccessPolicy]
    }
    filter_class = EmailDeviceFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, EmailDevice.objects.all()
        )

    @action(detail=False, methods=['post'], url_path='send')
    def send_token_to_emails(self, request, *args, **kwargs):
        send_token_to_email_devices(request.user)
        return Response(status=status.HTTP_200_OK)
