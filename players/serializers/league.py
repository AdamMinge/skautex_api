# Third-Party import
from rest_framework import serializers
# Local import
from players.models import League


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'league-detail', 'lookup_field': 'id'},
        }
