# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from accounts.models import AuditEntry
from accounts.serializers import AuditEntrySerializer
from accounts.policies import AuditEntryAccessPolicy
from accounts.filters import AuditEntryFilter


class AuditEntryViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    permission_classes = (AuditEntryAccessPolicy,)
    serializer_class = AuditEntrySerializer
    filter_class = AuditEntryFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=AuditEntry)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, AuditEntry.objects.all()
        )
