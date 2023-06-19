# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Local import
from core.backends.azure_storage import AzureMediaStorage
from linked_files.utils import create_lined_file_path


class LinkedFile(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    file = models.FileField(storage=AzureMediaStorage(), upload_to=create_lined_file_path)

    class Meta:
        verbose_name = "Linked File"
        verbose_name_plural = "Linked Files"
