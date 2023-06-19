# Third-Party import
import rest_framework_filters as filters
# Local import
from otp_auth.models import OrganizationAPIKey
from otp_auth.filters import OrganizationFilter
from otp_auth.models import Organization


class OrganizationApiKeyFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    created = filters.DateTimeFilter(field_name='created')
    expiry_date = filters.DateTimeFilter(field_name='expiry_date')
    revoked = filters.AutoFilter(lookups=['exact'], field_name='revoked')
    organization = filters.ModelChoiceFilter(field_name='organization',
                                             queryset=Organization.objects.all())

    order = filters.OrderingFilter(fields={'name': 'name', 'created': 'created',
                                           'expiry_date': 'expiry_date', 'revoked': 'revoked',
                                           'organization__name': 'organization'})

    class Meta:
        model = OrganizationAPIKey
        fields = []
