# Django import
from django.db import IntegrityError, transaction
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from players.models import Player
from reports.models import Report
from reports.constants import Messages
from reports.utils import create_player_report


class ReportNestedOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    owner = ReportNestedOwnerSerializer()

    class Meta:
        model = Report
        fields = ['url', 'title', 'owner', 'open_date', 'close_date', 'description', 'type']
        extra_kwargs = {
            'url': {'view_name': 'report-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['owner', 'open_date', 'close_date']


class ReportCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_report": Messages.CANNOT_CREATE_REPORT_ERROR
    }

    players = serializers.HyperlinkedRelatedField(view_name='player-detail', lookup_field='id', write_only=True,
                                                  many=True, read_only=False, queryset=Player.objects.all())
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Report
        fields = ['url', 'title', 'owner', 'open_date', 'close_date', 'description', 'players', 'type']
        extra_kwargs = {
            'url': {'view_name': 'report-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['open_date', 'close_date']

    def create(self, validated_data):
        players = validated_data.pop('players')
        try:
            with transaction.atomic():
                report = Report.objects.create(**validated_data)
                for player in players:
                    create_player_report(report=report, player=player)
        except IntegrityError:
            self.fail("cannot_create_report")
        return report
