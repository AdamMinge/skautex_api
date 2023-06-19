# Third-Party import
import rest_framework_filters as filters
# Local import
from rankings.models import Ranking


class RankingFilter(filters.FilterSet):
    order = filters.OrderingFilter(fields={'score': 'score'})

    class Meta:
        model = Ranking
        fields = []
