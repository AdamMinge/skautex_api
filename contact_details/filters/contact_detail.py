# Third-Party import
import rest_framework_filters as filters
# Local import
from contact_details.models import ContactDetail


class ContactDetailFilter(filters.FilterSet):
    type = filters.AutoFilter(lookups=['exact'], field_name='type')
    value = filters.AutoFilter(lookups=['exact', 'contains'], field_name='value')

    order = filters.OrderingFilter(fields=['type', 'value'])

    class Meta:
        model = ContactDetail
        fields = []
