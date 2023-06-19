# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from calendars.serializers import EventsTypesSerializer
from calendars.policies import EventsTypesAccessPolicy
from calendars.filters import EventsTypesFilter
from calendars.models import EventsTypes


class EventsTypesViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):

    permission_classes = (EventsTypesAccessPolicy,)
    serializer_class = EventsTypesSerializer
    filter_class = EventsTypesFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, EventsTypes.objects.all()
        )
