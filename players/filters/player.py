# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import Team, Player, League


class PlayerFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    surname = filters.AutoFilter(lookups=['exact', 'contains'], field_name='surname')
    position = filters.AutoFilter(lookups=['exact', 'contains'], field_name='position')
    birth_date = filters.DateFilter(field_name='birth_date')
    country = filters.AutoFilter(lookups=['exact', 'contains'], field_name='country')
    city = filters.AutoFilter(lookups=['exact', 'contains'], field_name='city')
    team = filters.ModelChoiceFilter(field_name='team', queryset=Team.objects.all())
    league = filters.ModelChoiceFilter(field_name='league', queryset=League.objects.all())

    order = filters.OrderingFilter(fields={'name': 'name', 'surname': 'surname',
                                           'position': 'position', 'birth_date': 'birth_date',
                                           'country': 'country', 'city': 'city',
                                           'team__name': 'team', 'league__name': 'league'})

    class Meta:
        model = Player
        fields = []
