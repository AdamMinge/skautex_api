# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
# Local import
from linked_files.models import LinkedFile
from cost_recording.models import CostRecording
from cost_recording.constants import Messages


class UserCostRecordingFileSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_cost_recording_id': 'object_id',
        'user_id': 'object_id',
    }

    default_error_messages = {
        "cannot_create_user_cost_recording_file": Messages.CANNOT_CREATE_USER_COST_RECORDING_FILE_ERROR
    }

    class Meta:
        model = LinkedFile
        fields = ['url', 'file']
        extra_kwargs = {
            'url': {'view_name': 'user_cost_recording_file-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        cost_recording = CostRecording.objects.get(id=self.context["view"].kwargs["user_cost_recording_id"])
        validated_data["content_object"] = cost_recording
        try:
            cost_recording_file = LinkedFile.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_user_cost_recording_file")
        return cost_recording_file
