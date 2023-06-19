# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
from rest_framework import serializers
# Local import
from cost_recording.models import CostRecording


class UserCostRecordingNestedOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class UserCostRecordingSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_id': 'owner__id',
    }

    owner = UserCostRecordingNestedOwnerSerializer()

    class Meta:
        model = CostRecording
        fields = ['url', 'name', 'money', 'record_date', 'owner']
        extra_kwargs = {
            'url': {'view_name': 'user_cost_recording-detail', 'lookup_field': 'id'},
            'owner': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['owner', 'record_date']


class UserCostRecordingCreateUpdateSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_id': 'owner__id',
    }

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CostRecording
        fields = ['url', 'name', 'money', 'record_date', 'owner']
        extra_kwargs = {
            'url': {'view_name': 'user_cost_recording-detail', 'lookup_field': 'id'},
        }
