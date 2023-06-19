# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from otp_auth.models import OrganizationAPIKey
from otp_auth.serializers import OrganizationAPIKeySerializer
from otp_auth.policies import OrganizationApiKeyAccessPolicy
from otp_auth.filters import OrganizationApiKeyFilter


class OrganizationApiKeyViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):

    permission_classes = (OrganizationApiKeyAccessPolicy,)
    serializer_class = OrganizationAPIKeySerializer
    filter_class = OrganizationApiKeyFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=OrganizationAPIKey)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, OrganizationAPIKey.objects.filter(organization=self.kwargs['organization_id'])
        )

    def perform_create(self, serializer):
        _, prefix, hashed_key = OrganizationAPIKey.objects.generate_key()
        serializer.save(prefix=prefix, hashed_key=hashed_key)


