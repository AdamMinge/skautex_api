# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from cost_recording.models import CostRecording
from cost_recording.constants import Messages


class CostRecordingNestedOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class CostRecordingSerializer(serializers.HyperlinkedModelSerializer):
    owner = CostRecordingNestedOwnerSerializer()

    class Meta:
        model = CostRecording
        fields = ['url', 'name', 'money', 'record_date', 'owner']
        extra_kwargs = {
            'url': {'view_name': 'cost_recording-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['owner', 'record_date']


class CostRecordingCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_cost_recording": Messages.CANNOT_CREATE_COST_RECORDING_ERROR
    }

    class Meta:
        model = CostRecording
        fields = ['url', 'name', 'money', 'record_date', 'owner']
        extra_kwargs = {
            'url': {'view_name': 'cost_recording-detail', 'lookup_field': 'id'},
            'owner': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
