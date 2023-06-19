# Third-Party import
from rest_framework import serializers
# Local import
from accounts.models import User


class UserPermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'user_permissions']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
            'user_permissions': {'view_name': 'permission-detail', 'lookup_field': 'id'},
        }
