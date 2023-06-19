# Django import
from django.contrib import admin
# Local import
from players.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city')
