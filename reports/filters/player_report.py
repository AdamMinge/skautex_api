# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import Player
from reports.models import PlayerReport


class PlayerReportFilter(filters.FilterSet):
    player = filters.ModelChoiceFilter(field_name='player', queryset=Player.objects.all())
    description = filters.AutoFilter(lookups=['exact', 'contains'], field_name='description')
    status = filters.AutoFilter(lookups=['exact'], field_name='status')

    order = filters.OrderingFilter(fields={'player': 'player', 'rating': 'rating',
                                           'description': 'description', 'status': 'status'})

    class Meta:
        model = PlayerReport
        fields = []
