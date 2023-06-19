# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
# Local import
from linked_files.models import LinkedFile
from reports.models import PlayerReport
from reports.constants import Messages


class PlayerReportFileSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'player_report_id': 'object_id',
    }

    default_error_messages = {
        "cannot_create_player_report_file": Messages.CANNOT_CREATE_PLAYER_REPORT_FILE_ERROR
    }

    class Meta:
        model = LinkedFile
        fields = ['url', 'file']
        extra_kwargs = {
            'url': {'view_name': 'player_report_file-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        player_report = PlayerReport.objects.get(id=self.context["view"].kwargs["player_report_id"])
        validated_data["content_object"] = player_report
        try:
            player_report_file = LinkedFile.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_player_report_file")
        return player_report_file
