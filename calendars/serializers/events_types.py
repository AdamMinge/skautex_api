# Third-Party import
from rest_framework import serializers
# Local import
from calendars.models import EventsTypes


class EventsTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventsTypes
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'events_types-detail', 'lookup_field': 'id'},
        }
