# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import Team


class TeamFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    country = filters.AutoFilter(lookups=['exact', 'contains'], field_name='country')
    city = filters.AutoFilter(lookups=['exact', 'contains'], field_name='city')

    order = filters.OrderingFilter(fields=['name', 'country', 'city'])

    class Meta:
        model = Team
        fields = []
