# Django import
from django.contrib import admin
# Local import
from reports.models import PlayerReportProfileStatistics


@admin.register(PlayerReportProfileStatistics)
class PlayerReportProfileStatisticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'content_object')
