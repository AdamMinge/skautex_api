# Django import
from django.contrib.auth.models import Permission
# Third-Party import
from rest_framework import serializers


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['url', 'name', 'codename']
        extra_kwargs = {
            'url': {'view_name': 'permission-detail', 'lookup_field': 'id'},
        }
