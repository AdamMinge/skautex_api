# Third-Party import
from rest_framework import viewsets
from django_otp.plugins.otp_totp.models import TOTPDevice
# Local import
from core import mixins
from otp_auth.serializers import TOTPDeviceSerializer, TOTPDeviceCreateSerializer
from otp_auth.policies import TOTPDeviceAccessPolicy
from otp_auth.filters import TOTPDeviceFilter


class TOTPDeviceView(mixins.MultiSerializerViewSetMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (TOTPDeviceAccessPolicy,)
    serializer_class = TOTPDeviceSerializer
    serializer_action_classes = {
        'create': TOTPDeviceCreateSerializer
    }
    filter_class = TOTPDeviceFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, TOTPDevice.objects.all()
        )
