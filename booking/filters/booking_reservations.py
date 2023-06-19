# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from booking.models import BookingObjects, BookingReservations


class BookingReservationsFilter(filters.FilterSet):
    booking_object = filters.ModelChoiceFilter(field_name='booking_object', queryset=BookingObjects.objects.all())
    user = filters.ModelChoiceFilter(field_name='user', queryset=get_user_model().objects.all())
    start_date = filters.IsoDateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.IsoDateTimeFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = BookingReservations
        fields = []


