# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers
# Local import
from otp_auth.models import Organization, OrganizationAPIKey
from otp_auth.constants import Messages


class OrganizationAPIKeySerializer(serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'organization_id': 'organization__id',
    }

    default_error_messages = {
        "cannot_create_organization_api_key": Messages.CANNOT_CREATE_ORGANIZATION_API_KEY_ERROR
    }

    class Meta:
        model = OrganizationAPIKey
        fields = ['url', 'name', 'created', 'expiry_date', 'revoked', 'prefix', 'hashed_key']
        extra_kwargs = {
            'url': {'view_name': 'organization_api_key-detail', 'lookup_field': 'id'},
            'organization': {'view_name': 'organization-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['organization']

    def create(self, validated_data):
        organization = Organization.objects.filter(id=self.context["view"].kwargs["organization_id"]).first()
        validated_data["organization"] = organization
        try:
            organization_api_key = OrganizationAPIKey.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_organization_api_key")
        return organization_api_key
