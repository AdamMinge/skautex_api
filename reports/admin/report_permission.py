# Django import
from django.contrib import admin
# Local import
from reports.models import ReportPermission


@admin.register(ReportPermission)
class ReportPermissionAdmin(admin.ModelAdmin):
    list_display = ('report', 'user', 'permission')
