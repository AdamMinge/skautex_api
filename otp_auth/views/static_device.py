# Third-Party import
from rest_framework import viewsets
from django_otp.plugins.otp_static.models import StaticDevice
# Local import
from core import mixins
from otp_auth.serializers import StaticDeviceSerializer, StaticDeviceCreateSerializer
from otp_auth.policies import StaticDeviceAccessPolicy
from otp_auth.filters import StaticDeviceFilter


class StaticDeviceView(mixins.MultiSerializerViewSetMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    permission_classes = (StaticDeviceAccessPolicy,)
    serializer_class = StaticDeviceSerializer
    serializer_action_classes = {
        'create': StaticDeviceCreateSerializer
    }
    filter_class = StaticDeviceFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, StaticDevice.objects.all()
        )
