# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import League


class LeagueFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    order = filters.OrderingFilter(fields=['name'])

    class Meta:
        model = League
        fields = []
