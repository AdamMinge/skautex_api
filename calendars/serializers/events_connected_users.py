# Django import
from django.db import IntegrityError
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
from rest_framework import serializers
# Local import
from calendars.models import EventsConnectedUsers, Events
from calendars.constants import Messages


class EventsConnectedUsersNestedUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class EventsConnectedUsersSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'event_id': 'event__id',
    }

    user = EventsConnectedUsersNestedUsersSerializer()

    class Meta:
        model = EventsConnectedUsers
        fields = ['url', 'user']
        extra_kwargs = {
            'url': {'view_name': 'connected_users-detail', 'lookup_field': 'id'},
        }


class EventsConnectedUsersCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'event_id': 'event__id',
    }

    default_error_messages = {
        "cannot_create_event_connected_users": Messages.CANNOT_CREATE_EVENT_CONNECTED_USERS_ERROR
    }

    class Meta:
        model = EventsConnectedUsers
        fields = ['url', 'user']
        extra_kwargs = {
            'url': {'view_name': 'connected_users-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        event = Events.objects.filter(id=self.context["view"].kwargs["event_id"]).first()
        validated_data["event"] = event
        try:
            event_connected_user = EventsConnectedUsers(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_event_connected_users")
        return event_connected_user
