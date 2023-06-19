# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Third-Party import
from djchoices import DjangoChoices, ChoiceItem


class ContactDetailTypeChoice(DjangoChoices):
    PHONE = ChoiceItem('phone')
    EMAIL = ChoiceItem('email')


class ContactDetail(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    type = models.CharField(max_length=5, choices=ContactDetailTypeChoice.choices)
    value = models.CharField(max_length=128)
