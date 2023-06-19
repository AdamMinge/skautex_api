# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from booking.models import BookingObjects, BookingBlacklist


class BookingBlacklistFilter(filters.FilterSet):
    booking_object = filters.ModelChoiceFilter(field_name='booking_object', queryset=BookingObjects.objects.all())
    user = filters.ModelChoiceFilter(field_name='user', queryset=get_user_model().objects.all())
    description = filters.AutoFilter(lookups=['exact', 'contains'], field_name='description')

    class Meta:
        model = BookingBlacklist
        fields = []


