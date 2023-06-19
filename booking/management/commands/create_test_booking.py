# Django import
from django.core.management.base import BaseCommand
# Local import
from booking.tests import (create_test_booking_objects_types, create_test_booking_objects,
                           create_test_booking_blacklist, create_test_booking_reservations)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_test_booking_objects_types()
        create_test_booking_objects()
        create_test_booking_blacklist()
        create_test_booking_reservations()
