# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from core.validators import StartBeforeEndDateValidator
from booking.models import BookingObjects, BookingReservations
from booking.validators import FreeDateValidator


class BookingReservationsNestedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class BookingReservationsNestedBookingObjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingObjects
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class BookingReservationsSerializer(serializers.HyperlinkedModelSerializer):
    booking_object = BookingReservationsNestedBookingObjectsSerializer()
    user = BookingReservationsNestedUserSerializer()

    class Meta:
        model = BookingReservations
        fields = ['url', 'booking_object', 'user', 'start_date', 'end_date']
        extra_kwargs = {
            'url': {'view_name': 'booking_reservations-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['booking_object', 'user']


class BookingReservationsCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BookingReservations
        validators = [StartBeforeEndDateValidator(), FreeDateValidator()]
        fields = ['url', 'booking_object', 'user', 'start_date', 'end_date']
        extra_kwargs = {
            'url': {'view_name': 'booking_reservations-detail', 'lookup_field': 'id'},
            'booking_object': {'view_name': 'booking_objects-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
