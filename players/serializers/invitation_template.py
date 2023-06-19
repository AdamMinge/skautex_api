# Third-Party import
from rest_framework import serializers
# Local import
from players.models import InvitationTemplate


class InvitationTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvitationTemplate
        fields = ['url', 'name', 'template']
        extra_kwargs = {
            'url': {'view_name': 'invitation_template-detail', 'lookup_field': 'id'},
        }
