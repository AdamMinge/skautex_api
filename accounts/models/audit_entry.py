# Python import
from datetime import datetime
# Django import
from django.db import models
# Local import
from accounts.models.user import User


class AuditEntry(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    logged_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="audit_entries")

    class Meta:
        verbose_name = "Audit Entry"
        verbose_name_plural = "Audit Entries"
