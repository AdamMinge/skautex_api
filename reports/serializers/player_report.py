# Third-Party import
from rest_framework import serializers
# Local import
from players.models import Player
from reports.models import PlayerReport, PlayerReportProfiles, PlayerReportProfileStatistics


class PlayerReportProfileNestedStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerReportProfileStatistics
        fields = ['name', 'value']


class PlayerReportProfileNestedStatisticsGroupSerializer(serializers.ModelSerializer):
    statistics = PlayerReportProfileNestedStatisticsSerializer(many=True)

    class Meta:
        model = PlayerReportProfileStatistics
        fields = ['name', 'statistics']


class PlayerReportNestedProfileSerializer(serializers.ModelSerializer):
    statistics = PlayerReportProfileNestedStatisticsSerializer(many=True)
    groups = PlayerReportProfileNestedStatisticsGroupSerializer(many=True)

    class Meta:
        model = PlayerReportProfiles
        fields = ['name', 'description', 'statistics', 'groups']


class PlayerReportNestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'surname']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'surname']


class PlayerReportSerializer(serializers.HyperlinkedModelSerializer):
    profiles = PlayerReportNestedProfileSerializer(many=True)
    player = PlayerReportNestedPlayerSerializer()

    class Meta:
        model = PlayerReport
        fields = ['url', 'report', 'player', 'score', 'description', 'profiles', 'status']
        extra_kwargs = {
            'url': {'view_name': 'player_report-detail', 'lookup_field': 'id'},
            'report': {'view_name': 'report-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['report', 'score']
