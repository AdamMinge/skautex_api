# Third-Party import
from rest_framework import serializers
# Local import
from players.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name', 'country', 'city']
        extra_kwargs = {
            'url': {'view_name': 'team-detail', 'lookup_field': 'id'},
        }
