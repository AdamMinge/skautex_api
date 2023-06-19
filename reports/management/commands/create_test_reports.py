# Django import
from django.core.management.base import BaseCommand
# Local import
from reports.tests import (create_test_report, create_test_report_permission,
                           create_test_player_report_statistics, create_test_player_report_statistics_type)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_report()
        create_test_report_permission()
        create_test_player_report_statistics_type()
        create_test_player_report_statistics()
