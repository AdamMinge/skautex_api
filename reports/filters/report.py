# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from reports.models import Report


class ReportFilter(filters.FilterSet):
    title = filters.AutoFilter(lookups=['exact', 'contains'], field_name='title')
    owner = filters.ModelChoiceFilter(field_name='owner', queryset=get_user_model().objects.all())
    open_date = filters.IsoDateTimeFilter(field_name='open_date', lookup_expr='gte')
    close_date = filters.IsoDateTimeFilter(field_name='close_date', lookup_expr='lte')
    description = filters.AutoFilter(lookups=['exact', 'contains'], field_name='description')
    type = filters.AutoFilter(lookups=['exact'], field_name='type')

    order = filters.OrderingFilter(fields={'title': 'title', 'owner__username': 'owner',
                                           'open_date': 'open_date', 'close_date': 'close_date',
                                           'description': 'description', 'type': 'type'})

    class Meta:
        model = Report
        fields = []
