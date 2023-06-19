# Django import
from django.utils.translation import ugettext_lazy as _
# Third-Party import
from rest_framework import serializers
from rest_framework.utils.representation import smart_repr
# Local import
from booking.models import BookingReservations


class FreeDateValidator:
    message = _('{booking_object} should not be reserved already in this time interval.')

    def __init__(self, booking_object_field='booking_object', start_date_field='start_date',
                 end_date_field='end_date', message=None):
        self.booking_object_field = booking_object_field
        self.start_date_field = start_date_field
        self.end_date_field = end_date_field
        self.message = message or self.message

    def __call__(self, attrs):
        booking_object = attrs[self.booking_object_field]
        start_date = attrs[self.start_date_field]
        end_date = attrs[self.end_date_field]
        already_reserved = BookingReservations.objects.filter(booking_object=booking_object,
                                                              start_date__gte=end_date,
                                                              end_date__gte=start_date).count() > 0

        if already_reserved:
            message = self.message.format(booking_object=self.booking_object_field)
            raise serializers.ValidationError(message, code='date_before_present')

    def __repr__(self):
        return '<%s(date_field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.booking_object_field)
        )
