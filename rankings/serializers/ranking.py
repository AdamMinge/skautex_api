# Third-Party import
from rest_framework import serializers
# Local import
from players.models import Player
from rankings.models import Ranking


class RankingNestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'surname', 'position']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'surname', 'position']


class RankingSerializer(serializers.HyperlinkedModelSerializer):
    player = RankingNestedPlayerSerializer()

    class Meta:
        model = Ranking
        fields = ['player', 'score']
        read_only_fields = ['player', 'score']
