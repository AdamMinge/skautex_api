# Django import
from django.contrib.auth import get_user_model
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
# Local import
from contact_details.models import ContactDetail
from accounts.constants import Messages


class UserContactDetailSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_id': 'object_id',
    }

    default_error_messages = {
        "cannot_create_user_contact_detail": Messages.CANNOT_CREATE_USER_CONTACT_DETAIL_ERROR
    }

    class Meta:
        model = ContactDetail
        fields = ['url', 'type', 'value']
        extra_kwargs = {
            'url': {'view_name': 'user_contact_detail-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        user = get_user_model().objects.get(id=self.context["view"].kwargs["user_id"])
        validated_data["content_object"] = user
        try:
            contact_detail = ContactDetail.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_user_contact_detail")
        return contact_detail
