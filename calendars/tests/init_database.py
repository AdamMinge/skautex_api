# Python import
from random import randint
from datetime import datetime, timedelta
# Local import
from calendars.models import Events, EventsTypes, EventsConnectedUsers
from accounts.tests import create_test_users


def __get_random(elements):
    return elements[randint(0, len(elements) - 1)]


def create_test_events():
    events = dict()
    events_types = list(create_test_events_types().values())
    users = list(create_test_users().values())
    colors = ['#ffffff', '#00ffff', '#ff00ff', '#ffff00', '#00ff00', '#0000ff', '#ff0000']

    for nr in range(30):
        start_date = datetime.now() + timedelta(days=nr + randint(2, 4))
        end_date = start_date + timedelta(days=randint(1, 2))
        event_type = __get_random(events_types)
        name = event_type.name + f' {nr}'
        descriptions = name + f' descriptions'

        events['event{}'.format(nr)], _ = Events.objects.get_or_create(
            name=name, description=descriptions, start_date=start_date, end_date=end_date,
            owner=__get_random(users), type=event_type, color=__get_random(colors))

    return events


def create_test_events_types():
    events_types = dict()
    events_types['Event'], _ = EventsTypes.objects.get_or_create(name='Event')
    events_types['Task'], _ = EventsTypes.objects.get_or_create(name='Task')
    return events_types


def create_test_events_connected_users():
    events = list(create_test_events().values())
    user = list(create_test_users().values())

    for event in events:
        connected_users = set()
        for nr in range(randint(0, 4)):
            connected_users.add(__get_random(user))
        for connected_user in connected_users:
            EventsConnectedUsers.objects.get_or_create(user=connected_user, event=event)
