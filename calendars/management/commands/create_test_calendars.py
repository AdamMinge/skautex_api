# Django import
from django.core.management.base import BaseCommand
# Local import
from calendars.tests import create_test_events_types, create_test_events, create_test_events_connected_users


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_events_types()
        create_test_events()
        create_test_events_connected_users()
