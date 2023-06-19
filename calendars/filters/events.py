# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from calendars.models import Events, EventsTypes


class EventsFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    description = filters.AutoFilter(lookups=['exact', 'contains'], field_name='description')
    start_date = filters.IsoDateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.IsoDateTimeFilter(field_name='end_date', lookup_expr='lte')
    color = filters.AutoFilter(lookups=['exact', 'contains'], field_name='color')
    status = filters.AutoFilter(lookups=['exact', 'contains'], field_name='status')
    type = filters.ModelChoiceFilter(field_name='type', queryset=EventsTypes.objects.all())
    hide = filters.AutoFilter(lookups=['exact', 'contains'], field_name='hide')
    owner = filters.ModelChoiceFilter(field_name='owner', queryset=get_user_model().objects.all())

    has_connected_user = filters.BooleanFilter(method='filter_has_connected_user')

    order = filters.OrderingFilter(fields={'name': 'name', 'status': 'status',
                                           'start_date': 'start_date', 'end_date': 'end_date'})

    class Meta:
        model = Events
        fields = []

    def filter_has_connected_user(self, qs, name, value):
        return qs.filter(event_connected_users__isnull=value)
