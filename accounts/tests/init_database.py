# Django import
from django.contrib.auth import models as auth_models
# Local import
from accounts.utils import create_user


def __link_groups_with_permissions(groups):
    permissions_list = list(auth_models.Permission.objects.all())
    groups['Director'].permissions.add(*permissions_list)
    groups['Scout'].permissions.add(*permissions_list)
    groups['Trainer'].permissions.add(*permissions_list)


def __link_users_with_groups(users):
    groups = create_test_groups()
    users['Trainer#1'].groups.add(groups['Trainer'])
    users['Trainer#2'].groups.add(groups['Trainer'])
    users['Trainer#3'].groups.add(groups['Trainer'])
    users['Trainer#4'].groups.add(groups['Trainer'])
    users['Trainer#5'].groups.add(groups['Trainer'])
    users['Scout#1'].groups.add(groups['Scout'])
    users['Scout#2'].groups.add(groups['Scout'])
    users['Scout#3'].groups.add(groups['Scout'])
    users['Scout#4'].groups.add(groups['Scout'])
    users['Director#1'].groups.add(groups['Director'])


def create_test_groups():
    groups = dict()
    groups['Trainer'], _ = auth_models.Group.objects.get_or_create(name='Trainer')
    groups['Scout'], _ = auth_models.Group.objects.get_or_create(name='Scout')
    groups['Director'], _ = auth_models.Group.objects.get_or_create(name='Director')
    __link_groups_with_permissions(groups)
    return groups


def create_test_users():
    users = dict()
    users['Trainer#1'] = create_user(username='Trainer#1', password='uzumymwuzumymw')
    users['Trainer#2'] = create_user(username='Trainer#2', password='uzumymwuzumymw')
    users['Trainer#3'] = create_user(username='Trainer#3', password='uzumymwuzumymw')
    users['Trainer#4'] = create_user(username='Trainer#4', password='uzumymwuzumymw')
    users['Trainer#5'] = create_user(username='Trainer#5', password='uzumymwuzumymw')
    users['Scout#1'] = create_user(username='Scout#1', password='uzumymwuzumymw')
    users['Scout#2'] = create_user(username='Scout#2', password='uzumymwuzumymw')
    users['Scout#3'] = create_user(username='Scout#3', password='uzumymwuzumymw')
    users['Scout#4'] = create_user(username='Scout#4', password='uzumymwuzumymw')
    users['Director#1'] = create_user(username='Director#1', password='uzumymwuzumymw')
    __link_users_with_groups(users)
    return users


def create_test_user_contact_detail():
    pass
