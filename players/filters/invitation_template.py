# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import InvitationTemplate


class InvitationTemplateFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    order = filters.OrderingFilter(fields={'name': 'name', })

    class Meta:
        model = InvitationTemplate
        fields = []
