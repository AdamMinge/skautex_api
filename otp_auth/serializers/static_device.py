# Django import
from django.db import IntegrityError, transaction
# Third-Party import
from rest_framework import serializers
from django_otp.plugins.otp_static.models import StaticDevice, StaticToken
# Local import
from otp_auth.constants import Messages


class StaticDeviceSerializer(serializers.HyperlinkedModelSerializer):
    tokens = serializers.SlugRelatedField(many=True, read_only=True, slug_field='token', source='token_set')

    class Meta:
        model = StaticDevice
        fields = ['url', 'user', 'name', 'confirmed', 'tokens']
        extra_kwargs = {
            'url': {'view_name': 'static_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed', 'tokens', 'user']


class StaticDeviceCreateSerializer(serializers.HyperlinkedModelSerializer):
    tokens = serializers.SlugRelatedField(many=True, read_only=True, slug_field='token', source='token_set')
    token_count = serializers.IntegerField(min_value=1, max_value=6, write_only=True, default=4, required=False)

    default_error_messages = {
        "cannot_create_static_device": Messages.CANNOT_CREATE_STATIC_DEVICE_ERROR
    }

    class Meta:
        model = StaticDevice
        fields = ['url', 'name', 'confirmed', 'token_count', 'tokens']
        extra_kwargs = {
            'url': {'view_name': 'static_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed', 'tokens']

    def __user_arg_used(self):
        return 'user' in self.context['request'].data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.__user_arg_used():
            self.Meta.fields = list(self.Meta.fields)
            self.Meta.fields.append('user')

    def create(self, validated_data):
        try:
            static_device = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_static_device")
        return static_device

    def perform_create(self, validated_data):
        static_device_data = validated_data
        if not self.__user_arg_used():
            static_device_data['user'] = self.context['request'].user
        token_count = static_device_data.pop('token_count')

        with transaction.atomic():
            static_device = StaticDevice.objects.create(**static_device_data)
            for n in range(token_count):
                token = StaticToken.random_token()
                static_device.token_set.create(token=token)
        return static_device
