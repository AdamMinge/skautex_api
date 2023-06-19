# Django import
from django.core.management.base import BaseCommand
# Local import
from accounts.tests import create_test_groups, create_test_users


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_groups()
        create_test_users()
