# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework import serializers
from django_otp.plugins.otp_email.models import EmailDevice
# Local import
from otp_auth.constants import Messages


class EmailDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailDevice
        fields = ['url', 'user', 'name', 'confirmed', 'email']
        extra_kwargs = {
            'url': {'view_name': 'email_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed', 'user']


class EmailDeviceCreateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "cannot_create_email_device": Messages.CANNOT_CREATE_EMAIL_DEVICE_ERROR
    }

    class Meta:
        model = EmailDevice
        fields = ['url', 'name', 'confirmed', 'email']
        extra_kwargs = {
            'url': {'view_name': 'email_device-detail', 'lookup_field': 'id'},
            'user': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['confirmed']

    def __user_arg_used(self):
        if 'request' in self.context:
            return 'user' in self.context['request'].data
        return False

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
                email_device = EmailDevice.objects.create(**validated_data)
            except IntegrityError:
                self.fail("cannot_create_email_device")
            return email_device
