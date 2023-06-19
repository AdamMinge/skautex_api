# Django import
from django.contrib import admin
# Local import
from accounts.models import AuditEntry


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ('ip', 'logged_date', 'user')

