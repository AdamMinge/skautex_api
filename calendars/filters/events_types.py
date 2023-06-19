# Third-Party import
import rest_framework_filters as filters
# Local import
from calendars.models import EventsTypes


class EventsTypesFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    class Meta:
        model = EventsTypes
        fields = []
