# Django import
from django.contrib import admin
# Local import
from players.models import Invitation


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('owner', 'player', 'creation_date', 'invitation_file')
