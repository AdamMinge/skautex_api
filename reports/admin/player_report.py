# Django import
from django.contrib import admin
# Local import
from reports.models import PlayerReport


@admin.register(PlayerReport)
class PlayerReportAdmin(admin.ModelAdmin):
    list_display = ('player', 'description', 'status')
