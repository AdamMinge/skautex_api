# Python import
import os
# Django import
from django.db import transaction
from django.contrib.auth import get_user_model
# Third-Party import
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_email.models import EmailDevice


def create_user(**kwargs):
    with transaction.atomic():
        user, _ = get_user_model().objects.get_or_create(**kwargs)
        user.set_password(kwargs['password'])
        user.save()

        TOTPDevice.objects.get_or_create(name='default', digits=6, user=user)
        EmailDevice.objects.get_or_create(name='default', user=user)
    return user


def create_superuser(**kwargs):
    with transaction.atomic():
        user = get_user_model().objects.create_superuser(**kwargs)
        TOTPDevice.objects.create(name='default', digits=6, user=user)
        EmailDevice.objects.create(name='default', user=user)
    return user


def get_user_by_id(request, user_id):
    if user_id == 'me':
        return request.user
    else:
        return get_user_model().objects.get(id=int(user_id))


def create_user_profile_picture_path(instance, filename):
    return os.path.join(
        'users',
        filename
    )

