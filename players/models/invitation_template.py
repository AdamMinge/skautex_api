# Django import
from django.core.validators import FileExtensionValidator
from django.db import models
# Local import
from core.backends.azure_storage import AzureMediaStorage
from players.utils import create_invitation_template_path


class InvitationTemplate(models.Model):
    name = models.CharField(max_length=128)
    template = models.FileField(storage=AzureMediaStorage(), upload_to=create_invitation_template_path,
                                validators=[FileExtensionValidator(allowed_extensions=['docx'])])

    class Meta:
        verbose_name = "Invitation Template"
        verbose_name_plural = "Invitation Templates"
