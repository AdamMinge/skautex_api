# Third-Party import
import rest_framework_filters as filters
# Local import
from otp_auth.models import Organization


class OrganizationFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    active = filters.AutoFilter(lookups=['exact'], field_name='active')

    order = filters.OrderingFilter(fields=['name', 'active'])

    class Meta:
        model = Organization
        fields = []
