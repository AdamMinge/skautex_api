# Python import
from random import randint
from datetime import datetime, timedelta
# Local import
from booking.models import BookingObjects, BookingObjectsTypes, BookingBlacklist, BookingReservations
from accounts.tests import create_test_users


def __get_random(elements):
    return elements[randint(0, len(elements) - 1)]


def create_test_booking_blacklist():
    booking_objects = list(create_test_booking_objects().values())
    users = list(create_test_users().values())
    descriptions = ['abuse', 'notorious lateness', 'too little internship']

    for nr in range(10):
        BookingBlacklist.objects.get_or_create(booking_object=__get_random(booking_objects),
                                               user=__get_random(users), description=__get_random(descriptions))


def create_test_booking_reservations():
    booking_objects = list(create_test_booking_objects().values())
    users = list(create_test_users().values())

    for booking_object in booking_objects:
        for nr in range(10):
            start_date = datetime.now() + timedelta(days=nr + randint(2, 4))
            end_date = start_date + timedelta(days=randint(1, 2))
            BookingReservations.objects.get_or_create(booking_object=booking_object,
                                                      user=__get_random(users),
                                                      start_date=start_date, end_date=end_date)


def create_test_booking_objects():
    booking_objects = dict()
    booking_objects_types = create_test_booking_objects_types()

    for nr in range(10):
        phone_name = 'Phone{}'.format(nr)
        car_name = 'Car{}'.format(nr)
        laptop_name = 'Laptop{}'.format(nr)

        booking_objects[phone_name], _ = BookingObjects.objects.get_or_create(
            name=phone_name, type=booking_objects_types['Phone'])
        booking_objects[car_name], _ = BookingObjects.objects.get_or_create(
            name=car_name, type=booking_objects_types['Car'])
        booking_objects[laptop_name], _ = BookingObjects.objects.get_or_create(
            name=laptop_name, type=booking_objects_types['Laptop'])

    return booking_objects


def create_test_booking_objects_types():
    booking_objects_types = dict()
    booking_objects_types['Phone'], _ = BookingObjectsTypes.objects.get_or_create(name='Phone')
    booking_objects_types['Car'], _ = BookingObjectsTypes.objects.get_or_create(name='Car')
    booking_objects_types['Laptop'], _ = BookingObjectsTypes.objects.get_or_create(name='Laptop')
    return booking_objects_types
