# Django import
from django.db import IntegrityError, transaction
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from core.validators import StartBeforeEndDateValidator
from calendars.models import Events, EventsTypes, EventsConnectedUsers
from calendars.constants import Messages


class EventsNestedEventsTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventsTypes
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'events_types-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class EventsNestedUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    type = EventsNestedEventsTypesSerializer()
    owner = EventsNestedUsersSerializer()

    class Meta:
        model = Events
        fields = ['url', 'name', 'description', 'start_date',
                  'end_date', 'owner', 'type', 'status', 'hide', 'color']
        extra_kwargs = {
            'url': {'view_name': 'events-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['type']


class EventsCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_event": Messages.CANNOT_CREATE_EVENT_ERROR,
        "cannot_update_event": Messages.CANNOT_UPDATE_EVENT_ERROR
    }

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    connected_users = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='id', write_only=True,
                                                          many=True, read_only=False, queryset=get_user_model().objects.all())

    class Meta:
        model = Events
        validators = [StartBeforeEndDateValidator()]
        fields = ['url', 'name', 'description', 'start_date',
                  'end_date', 'owner', 'type', 'status', 'hide', 'color', 'connected_users']
        extra_kwargs = {
            'url': {'view_name': 'events-detail', 'lookup_field': 'id'},
            'owner': {'view_name': 'user-detail', 'lookup_field': 'id'},
            'type': {'view_name': 'events_types-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        connected_users = validated_data.pop('connected_users')
        try:
            with transaction.atomic():
                event = Events.objects.create(**validated_data)
                for connected_user in connected_users:
                    EventsConnectedUsers.objects.create(event=event, user=connected_user)
        except IntegrityError:
            self.fail("cannot_create_event")
        return event

    def update(self, instance, validated_data):
        connected_users = validated_data.pop('connected_users')
        try:
            super().update(instance, validated_data)
            with transaction.atomic():
                instance.event_connected_users.all().delete()
                for connected_user in connected_users:
                    EventsConnectedUsers.objects.create(event=instance, user=connected_user)
        except IntegrityError:
            self.fail("cannot_update_event")
        return instance

