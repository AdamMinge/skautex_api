# Local import
from django.conf import settings
# Third-Party import
from django_otp import devices_for_user, match_token
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_static.models import StaticDevice
from django_otp.plugins.otp_email.models import EmailDevice
# Local Import
from accounts.models import AuditEntry


def get_user_totp_devices(user, confirmed=None):
    user_devices = []
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            user_devices.append(device)
    return user_devices


def get_user_static_devices(user, confirmed=None):
    user_devices = []
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, StaticDevice):
            user_devices.append(device)
    return user_devices


def get_user_email_devices(user, confirmed=None):
    user_devices = []
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, EmailDevice):
            user_devices.append(device)
    return user_devices


def send_token_to_email_devices(user):
    for device_email in get_user_email_devices(user):
        device_email.generate_challenge()


def verify_token(user, token, device=None):
    verification_debug_users = getattr(settings, 'VERIFICATION_DEBUG_USERS', [])
    verification_debug_code = getattr(settings, 'VERIFICATION_DEBUG_CODE', None)

    if user.username in verification_debug_users and token == verification_debug_code:
        if device is not None:
            device_verify_is_allowed, _ = device.verify_is_allowed()
            return device if device_verify_is_allowed else None
        else:
            matches = (d for d in devices_for_user(user) if d.verify_is_allowed())
            return next(matches)
    return match_token(user, token)


def user_first_verification(user):
    verification_debug_users = getattr(settings, 'VERIFICATION_DEBUG_USERS', [])
    return user.username in verification_debug_users or not AuditEntry.objects.filter(user=user).count()
