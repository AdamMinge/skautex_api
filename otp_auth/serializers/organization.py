# Third-Party import
from rest_framework import serializers
from rest_framework_nested import relations
# Local import
from otp_auth.models import Organization


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    api_keys = relations.NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='organization_api_key-detail',
        lookup_field='id',
        parent_lookup_kwargs={'organization_id': 'organization__id'}
    )

    class Meta:
        model = Organization
        fields = ['url', 'name', 'active', 'api_keys']
        extra_kwargs = {
            'url': {'view_name': 'organization-detail', 'lookup_field': 'id'},
        }
