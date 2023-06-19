# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from players.models import Invitation, Player


class InvitationFilter(filters.FilterSet):
    owner = filters.ModelChoiceFilter(field_name='owner', queryset=get_user_model().objects.all())
    player = filters.ModelChoiceFilter(field_name='player', queryset=Player.objects.all())
    creation_date = filters.IsoDateTimeFilter(field_name='creation_date', lookup_expr='gte')

    order = filters.OrderingFilter(fields={'owner__username': 'owner',
                                           'creation_date': 'creation_date'})

    class Meta:
        model = Invitation
        fields = []
