# Django import
from django.contrib import admin
# Local import
from players.models import League


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name',)
