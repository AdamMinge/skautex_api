# Django import
from django.contrib import admin
# Local import
from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'position', 'birth_date',
                    'country', 'city', 'profile_picture', 'team')
