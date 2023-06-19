# Django import
from django.db import IntegrityError
# Third-Party import
from rest_framework_nested import serializers as nested_serializers
# Local import
from contact_details.models import ContactDetail
from players.constants import Messages
from players.models import Player


class PlayerContactDetailSerializer(nested_serializers.NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'player_id': 'object_id',
    }

    default_error_messages = {
        "cannot_create_player_contact_detail": Messages.CANNOT_CREATE_PLAYER_CONTACT_DETAIL_ERROR
    }

    class Meta:
        model = ContactDetail
        fields = ['url', 'type', 'value']
        extra_kwargs = {
            'url': {'view_name': 'player_contact_detail-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        player = Player.objects.get(id=self.context["view"].kwargs["player_id"])
        validated_data["content_object"] = player
        try:
            contact_detail = ContactDetail.objects.create(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_player_contact_detail")
        return contact_detail
