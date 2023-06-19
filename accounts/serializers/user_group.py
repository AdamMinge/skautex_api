# Third-Party import
from rest_framework import serializers
# Local import
from accounts.models import User


class UserGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'groups']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
            'groups': {'view_name': 'group-detail', 'lookup_field': 'id'},
        }
