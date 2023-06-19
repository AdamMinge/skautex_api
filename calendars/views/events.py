# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from calendars.serializers import EventsSerializer, EventsCreateUpdateSerializer
from calendars.policies import EventsAccessPolicy
from calendars.filters import EventsFilter
from calendars.models import Events


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: EventsSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: EventsSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: EventsSerializer()}))
class EventsViewSet(mixins.MultiSerializerViewSetMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (EventsAccessPolicy,)
    serializer_class = EventsSerializer
    response_serializer = EventsSerializer
    serializer_action_classes = {
        'create': EventsCreateUpdateSerializer,
        'update': EventsCreateUpdateSerializer,
        'partial_update': EventsCreateUpdateSerializer,
    }
    filter_class = EventsFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=Events)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Events.objects.all()
        )
