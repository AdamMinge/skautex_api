# Django import
from django.dispatch import receiver
# Local import
from accounts.models.audit_entry import AuditEntry
from otp_auth.signals import user_verified


@receiver(user_verified)
def save_user_verification(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(ip=ip, user=user)
