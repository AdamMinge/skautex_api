# Django import
from django.contrib.auth import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
# Third-Party import
from rest_framework_api_key.models import APIKey
# Local import
from otp_auth.models import Organization, OrganizationAPIKey


def get_all_permissions():
    content_types = [
        ContentType.objects.get_for_model(LogEntry),
        ContentType.objects.get_for_model(ContentType),
        ContentType.objects.get_for_model(APIKey),
        ContentType.objects.get_for_model(Session),
        ContentType.objects.get_for_model(Organization),
        ContentType.objects.get_for_model(OrganizationAPIKey),
        ContentType.objects.get(app_label='db', model='testmodel')
    ]

    return models.Permission.objects.exclude(content_type__in=content_types)


def get_all_permissions_for_user(user):
    if user.is_staff:
        return get_all_permissions()

    permissions = user.user_permissions.all()
    for group in user.groups.all():
        permissions = permissions | group.permissions.all()
    return permissions.distinct()
