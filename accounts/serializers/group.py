# Django import
from django.contrib.auth.models import Group
# Third-Party import
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', 'permissions']
        extra_kwargs = {
            'url': {'view_name': 'group-detail', 'lookup_field': 'id'},
            'permissions': {'view_name': 'permission-detail', 'lookup_field': 'id'},
        }
