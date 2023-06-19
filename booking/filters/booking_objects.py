# Third-Party import
import rest_framework_filters as filters
# Local import
from booking.models import BookingObjects, BookingObjectsTypes


class BookingObjectsFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    type = filters.ModelChoiceFilter(field_name='type', queryset=BookingObjectsTypes.objects.all())

    order = filters.OrderingFilter(fields={'name': 'name', 'type__name': 'type', })

    class Meta:
        model = BookingObjects
        fields = []


