# Django import
from django.db import models
# Third-Party import
from rest_framework_api_key.models import AbstractAPIKey
# Local import
from otp_auth.managers import OrganizationAPIKeyManager
from otp_auth.models.organization import Organization


class OrganizationAPIKey(AbstractAPIKey):
    id = models.AutoField(primary_key=True, auto_created=True)

    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Organization API key"
        verbose_name_plural = "Organization API keys"

    objects = OrganizationAPIKeyManager()
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
