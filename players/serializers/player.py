# Third-Party import
from rest_framework import serializers
# Local import
from core.validators import DateBeforePresentValidator
from players.models import Player, Team, League
from players.constants import Messages


class PlayerNestedTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'team-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class PlayerNestedLeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ['url', 'name']
        extra_kwargs = {
            'url': {'view_name': 'league-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = PlayerNestedTeamSerializer()
    league = PlayerNestedLeagueSerializer()

    class Meta:
        model = Player
        fields = ['url', 'name', 'surname', 'position', 'birth_date', 'dominant_leg',
                  'country', 'city', 'profile_picture', 'team', 'league', 'status', 'is_active']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['profile_picture', 'is_active']


class PlayerCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_player": Messages.CANNOT_CREATE_PLAYER_ERROR
    }

    class Meta:
        model = Player
        validators = [DateBeforePresentValidator(date_field='birth_date')]
        fields = ['url', 'name', 'surname', 'position', 'birth_date', 'dominant_leg',
                  'country', 'city', 'profile_picture', 'team', 'league', 'status', 'is_active']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
            'team': {'view_name': 'team-detail', 'lookup_field': 'id'},
            'league': {'view_name': 'league-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['profile_picture', 'is_active']


class PlayerProfilePictureUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'profile_picture']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
