# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from booking.serializers import BookingObjectsTypesSerializer
from booking.policies import BookingObjectsTypesAccessPolicy
from booking.filters import BookingObjectsTypesFilter
from booking.models import BookingObjectsTypes


class BookingObjectsTypesViewSet(mixins.CreateModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):

    permission_classes = (BookingObjectsTypesAccessPolicy,)
    serializer_class = BookingObjectsTypesSerializer
    filter_class = BookingObjectsTypesFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, BookingObjectsTypes.objects.all()
        )
