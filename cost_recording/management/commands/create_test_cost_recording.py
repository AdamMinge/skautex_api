# Django import
from django.core.management.base import BaseCommand
# Local import
from cost_recording.test import create_test_cost_recording


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_cost_recording()
