# Third-Party import
from rest_framework import serializers
# Local import
from booking.models import BookingObjectsTypes, BookingObjects


class BookingObjectsNestedOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingObjectsTypes
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects_types-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class BookingObjectsSerializer(serializers.HyperlinkedModelSerializer):
    type = BookingObjectsNestedOwnerSerializer()

    class Meta:
        model = BookingObjects
        fields = ['url', 'name', 'type']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['type']


class BookingObjectsCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingObjects
        fields = ['url', 'name', 'type']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
            'type': {'view_name': 'booking_objects_types-detail', 'lookup_field': 'id'},
        }
