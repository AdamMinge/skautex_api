# Third-Party import
from rest_framework import serializers
# Local import
from booking.models import BookingObjectsTypes


class BookingObjectsTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingObjectsTypes
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects_types-detail', 'lookup_field': 'id'},
        }
