# Third-Party import
import rest_framework_filters as filters
# Local import
from booking.models import BookingObjectsTypes


class BookingObjectsTypesFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    order = filters.OrderingFilter(fields={'name': 'name'})

    class Meta:
        model = BookingObjectsTypes
        fields = []


