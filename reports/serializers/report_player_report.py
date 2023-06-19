# Django import
from django.db import IntegrityError, transaction
from django.contrib.admin.options import get_content_type_for_model
# Third-Party import
from rest_framework_nested import serializers as nested_serializer
from rest_framework import serializers
# Local import
from players.models import Player
from reports.models import (Report, PlayerReport, PlayerReportProfiles,
                            PlayerReportProfileStatistics, PlayerReportProfileStatisticsGroups)
from reports.constants import Messages
from reports.utils import create_player_report


class ReportPlayerReportProfileNestedStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerReportProfileStatistics
        fields = ['name', 'value']


class ReportPlayerReportProfileNestedStatisticsGroupSerializer(serializers.ModelSerializer):
    statistics = ReportPlayerReportProfileNestedStatisticsSerializer(many=True)

    class Meta:
        model = PlayerReportProfileStatistics
        fields = ['name', 'statistics']


class ReportPlayerReportNestedProfileSerializer(serializers.ModelSerializer):
    statistics = ReportPlayerReportProfileNestedStatisticsSerializer(many=True)
    groups = ReportPlayerReportProfileNestedStatisticsGroupSerializer(many=True)

    class Meta:
        model = PlayerReportProfiles
        fields = ['name', 'description', 'statistics', 'groups']


class ReportPlayerReportNestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'surname']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'surname']


class ReportPlayerReportGetSerializer(nested_serializer.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'report_id': 'report__id',
    }

    profiles = ReportPlayerReportNestedProfileSerializer(many=True)
    player = ReportPlayerReportNestedPlayerSerializer()

    class Meta:
        model = PlayerReport
        fields = ['url', 'report', 'player', 'score', 'description', 'profiles', 'status']
        extra_kwargs = {
            'url': {'view_name': 'player_report-detail', 'lookup_field': 'id'},
            'report': {'view_name': 'report-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['report', 'score']


class ReportPlayerReportCreateSerializer(nested_serializer.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'report_id': 'report__id',
    }

    default_error_messages = {
        "cannot_create_player_report": Messages.CANNOT_CREATE_PLAYER_REPORT_ERROR
    }

    class Meta:
        model = PlayerReport
        fields = ['url', 'player', 'description']
        extra_kwargs = {
            'url': {'view_name': 'player_report-detail', 'lookup_field': 'id'},
            'player': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        report = Report.objects.filter(id=self.context["view"].kwargs["report_id"]).first()
        validated_data["report"] = report
        try:
            player_report = create_player_report(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_player_report")
        return player_report


class ReportPlayerReportUpdateSerializer(nested_serializer.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'report_id': 'report__id',
    }

    default_error_messages = {
        "cannot_update_player_report": Messages.CANNOT_UPDATE_PLAYER_REPORT_ERROR
    }

    profiles = ReportPlayerReportNestedProfileSerializer(many=True, required=False)

    class Meta:
        model = PlayerReport
        fields = ['url', 'description', 'profiles']
        extra_kwargs = {
            'url': {'view_name': 'player_report-detail', 'lookup_field': 'id'},
        }

    def __update_statistic(self, container, name, value):
        statistic = PlayerReportProfileStatistics.objects.get(content_type=get_content_type_for_model(container),
                                                              object_id=container.id, name=name)
        statistic.value = value
        statistic.save()

    def __update_player_report(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        try:
            profiles = validated_data.get('profiles', [])
            for profile in profiles:
                profile_object = PlayerReportProfiles.objects.get(name=profile.get('name'),
                                                                  player_report=instance)
                profile_object.description = profile.get('description', profile_object.description)
                profile_object.save()

                groups = profile.get('groups', [])
                for group in groups:
                    group_object = PlayerReportProfileStatisticsGroups.objects.get(name=group.get('name'),
                                                                                   profile=profile_object)

                    group_statistics = group.get('statistics', [])
                    for statistic in group_statistics:
                        self.__update_statistic(group_object, statistic.get('name'), statistic.get('value'))

                statistics = profile.get('statistics', [])
                for statistic in statistics:
                    self.__update_statistic(profile_object, statistic.get('name'), statistic.get('value'))

        except (KeyError, PlayerReportProfiles.DoesNotExist,
                PlayerReportProfileStatisticsGroups.DoesNotExist,
                PlayerReportProfileStatistics.DoesNotExist):
            self.fail("cannot_update_player_report")

    def update(self, instance, validated_data):
        with transaction.atomic():
            self.__update_player_report(instance, validated_data)
        return instance
