# Python Import
import io
from datetime import datetime
# Django import
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import serializers
# Local import
from players.models import Player, Invitation, InvitationTemplate
from players.utils import InvitationDocument


class InvitationNestedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'surname']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'surname']


class InvitationNestedOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['username']


class InvitationNestedInvitationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationTemplate
        fields = ['url', 'name', 'template']
        extra_kwargs = {
            'url': {'view_name': 'invitation_template-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['name', 'template']


class InvitationGetSerializer(serializers.HyperlinkedModelSerializer):
    owner = InvitationNestedOwnerSerializer()
    player = InvitationNestedPlayerSerializer()
    trainer = InvitationNestedOwnerSerializer()
    invitation_template = InvitationNestedInvitationTemplateSerializer()

    class Meta:
        model = Invitation
        fields = ['url', 'owner', 'player', 'trainer', 'creation_date', 'invitation_file', 'invitation_template']
        extra_kwargs = {
            'url': {'view_name': 'invitation-detail', 'lookup_field': 'id'},
        }
        read_only_fields = ['owner', 'player', 'creation_date', 'invitation_file', 'invitation_template']


class InvitationCreateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = Invitation
        fields = ['url', 'invitation_template', 'owner', 'player', 'trainer', 'start_date', 'end_date']
        extra_kwargs = {
            'url': {'view_name': 'invitation-detail', 'lookup_field': 'id'},
            'player': {'view_name': 'player-detail', 'lookup_field': 'id'},
            'trainer': {'view_name': 'user-detail', 'lookup_field': 'id'},
            'invitation_template': {'view_name': 'invitation_template-detail', 'lookup_field': 'id'},
        }

    def create(self, validated_data):
        validated_data['creation_date'] = datetime.now()

        owner = validated_data['owner']
        player = validated_data['player']
        trainer = validated_data['trainer']
        invitation_template = validated_data['invitation_template']

        creation_date = validated_data['creation_date']
        start_date = validated_data.pop('start_date')
        end_date = validated_data.pop('end_date')

        document = InvitationDocument(invitation_template, player, owner, trainer,
                                      creation_date, start_date, end_date)

        file_stream = io.BytesIO()
        document.save(file_stream)
        file_stream.seek(0)

        instance = super().create(validated_data)
        instance.invitation_file.save(document.name() + f'_{instance.id}.docx', file_stream, save=True)
        return instance
