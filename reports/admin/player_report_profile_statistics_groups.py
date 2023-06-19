# Django import
from django.contrib import admin
# Local import
from reports.models import PlayerReportProfileStatisticsGroups


@admin.register(PlayerReportProfileStatisticsGroups)
class PlayerReportProfileStatisticsGroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')
