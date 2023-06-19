# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from booking.models import BookingObjects, BookingBlacklist


class BookingBlacklistNestedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class BookingBlacklistNestedBookingObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingObjects
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class BookingBlacklistSerializer(serializers.HyperlinkedModelSerializer):
    booking_object = BookingBlacklistNestedBookingObjectSerializer()
    user = BookingBlacklistNestedUserSerializer()

    class Meta:
        model = BookingBlacklist
        fields = ['url', 'booking_object', 'user', 'description']
        extra_kwargs = {
            'url': {'view_name': 'booking_blacklist-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['booking_object', 'user']


class BookingBlacklistCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingBlacklist
        fields = ['url', 'booking_object', 'user', 'description']
        extra_kwargs = {
            'url': {'view_name': 'booking_blacklist-detail', 'lookup_field': 'id'},
            'booking_object': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
