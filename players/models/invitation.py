# Python import
from datetime import datetime
# Django import
from django.db import models
from django.contrib.auth import get_user_model
# Local import
from core.backends.azure_storage import AzureMediaStorage
from players.models.player import Player
from players.models.invitation_template import InvitationTemplate
from players.utils import create_invitation_file_path


class Invitation(models.Model):
    invitation_file = models.FileField(storage=AzureMediaStorage(), upload_to=create_invitation_file_path)
    invitation_template = models.ForeignKey(InvitationTemplate, on_delete=models.CASCADE, related_name="invitations")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="owner_invitations")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="invitations")
    trainer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="trainer_invitations")
    creation_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Invitation"
        verbose_name_plural = "Invitations"
