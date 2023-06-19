# Django import
from django.contrib import admin
# Local import
from reports.models import PlayerReportProfiles


@admin.register(PlayerReportProfiles)
class PlayerReportProfilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'player_report')
