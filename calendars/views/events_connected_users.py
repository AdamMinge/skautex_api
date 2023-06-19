# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from calendars.serializers import EventsConnectedUsersCreateUpdateSerializer, EventsConnectedUsersSerializer
from calendars.policies import EventsConnectedUsersAccessPolicy
from calendars.filters import EventsConnectedUsersFilter
from calendars.models import EventsConnectedUsers


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: EventsConnectedUsersSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: EventsConnectedUsersSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: EventsConnectedUsersSerializer()}))
class EventsConnectedUsersViewSet(mixins.MultiSerializerViewSetMixin,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.ListModelMixin,
                                  viewsets.GenericViewSet):

    permission_classes = (EventsConnectedUsersAccessPolicy,)
    serializer_class = EventsConnectedUsersSerializer
    response_serializer = EventsConnectedUsersSerializer
    serializer_action_classes = {
        'create': EventsConnectedUsersCreateUpdateSerializer,
        'update': EventsConnectedUsersCreateUpdateSerializer,
        'partial_update': EventsConnectedUsersCreateUpdateSerializer,
    }
    filter_class = EventsConnectedUsersFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=EventsConnectedUsers)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, EventsConnectedUsers.objects.filter(event=self.kwargs['event_id'])
        )
