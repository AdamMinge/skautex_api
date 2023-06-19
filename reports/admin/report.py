# Django import
from django.contrib import admin
# Local import
from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'open_date', 'close_date', 'description', 'type')
