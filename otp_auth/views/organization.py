# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from otp_auth.models import Organization
from otp_auth.serializers import OrganizationSerializer
from otp_auth.policies import OrganizationAccessPolicy
from otp_auth.filters import OrganizationFilter


class OrganizationViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    permission_classes = (OrganizationAccessPolicy,)
    serializer_class = OrganizationSerializer
    filter_class = OrganizationFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Organization.objects.all()
        )
