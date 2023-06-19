# Django import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
# Local import
from core.backends.azure_storage import AzureMediaStorage
from contact_details.models import ContactDetail
from accounts.utils import create_user_profile_picture_path


class User(AbstractUser):
    profile_picture = models.ImageField(storage=AzureMediaStorage(),
                                        upload_to=create_user_profile_picture_path,
                                        blank=True, null=True)

    contact_details = GenericRelation(ContactDetail)
