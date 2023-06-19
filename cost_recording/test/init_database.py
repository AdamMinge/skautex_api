# python import
from datetime import datetime
from random import randint
# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import pytz
from djmoney.utils import Money
# Local import
from cost_recording.models import CostRecording


def __get_test_cost_recording_names():
    return ['hotel', 'benzine', 'sport clothes', 'training equipment',
            'staff education', 'meals', 'first aid']


def __create_test_cost_recording_for_user(owner, names):
    reports_count = randint(0, 100)

    for i in range(reports_count):
        name = names[randint(0, len(names) - 1)]
        money = Money(randint(1, 100), 'PLN')
        date = datetime(2020, randint(1, 12), randint(1, 28), randint(1, 23), randint(0, 59), tzinfo=pytz.UTC)
        CostRecording.objects.get_or_create(name=name, money=money, owner=owner, record_date=date)


def create_test_cost_recording():
    users_list = get_user_model().objects.all()
    cost_recordings_names = __get_test_cost_recording_names()

    for user in users_list:
        __create_test_cost_recording_for_user(user, cost_recordings_names)

