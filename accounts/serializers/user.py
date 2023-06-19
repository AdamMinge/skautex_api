# Django import
from django.db import IntegrityError
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password
# Third-Party import
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# Local import
from accounts.utils import create_user
from accounts.constants import Messages
from accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_active', 'profile_picture']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['is_active']


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": Messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email',
                  'is_active', 'password', 'profile_picture']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['is_active', 'profile_picture']

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")
        return user

    def perform_create(self, validated_data):
        return create_user(**validated_data)


class UserPasswordUpdateSerializer(serializers.HyperlinkedModelSerializer):
    default_error_messages = {
        "password_and_confirmation_password_error": Messages.PASSWORD_AND_CONFIRMATION_PASSWORD_ERROR
    }

    password1 = serializers.CharField(style={"input_type": "password1"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password2"}, write_only=True)

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def __validate_password(self, password1, password2):
        if password1 != password2:
            self.fail("password_and_confirmation_password_error")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")
        try:
            validate_password(password1, self.instance)
            self.__validate_password(password1, password2)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password1"))
        instance.save()
        return instance


class UserProfilePictureUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'profile_picture']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
