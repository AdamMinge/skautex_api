# Django import
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# Local import
from accounts.utils import create_superuser


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = getattr(settings, 'ADMIN_NAME', 'admin')
        password = getattr(settings, 'ADMIN_PASSWORD', 'admin')
        email = getattr(settings, 'ADMIN_MAIL', None)

        if not get_user_model().objects.filter(username=username).exists():
            create_superuser(username=username, password=password, email=email)
