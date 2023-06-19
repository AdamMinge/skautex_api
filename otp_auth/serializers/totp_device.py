# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework import serializers
from django_otp.plugins.otp_totp.models import TOTPDevice
# Local import
from otp_auth.constants import Messages


class TOTPDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TOTPDevice
        fields = ['url', 'user', 'name', 'confirmed', 'digits', 'config_url']
        extra_kwargs = {
            'url': {'view_name': 'totp_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed', 'digits', 'config_url', 'user']


class TOTPDeviceCreateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_totp_device": Messages.CANNOT_CREATE_TOTP_DEVICE_ERROR
    }

    class Meta:
        model = TOTPDevice
        fields = ['url', 'name', 'confirmed', 'digits', 'config_url']
        extra_kwargs = {
            'url': {'view_name': 'totp_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed', 'config_url']

    def __user_arg_used(self):
        return 'user' in self.context['request'].data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.__user_arg_used():
            self.Meta.fields = list(self.Meta.fields)
            self.Meta.fields.append('user')

    def create(self, validated_data):
        if self.__user_arg_used():
            return super().create(validated_data)
        else:
            validated_data['user'] = self.context['request'].user
            try:
                totp_device = TOTPDevice.objects.create(**validated_data)
            except IntegrityError:
                self.fail("cannot_create_totp_device")
            return totp_device
