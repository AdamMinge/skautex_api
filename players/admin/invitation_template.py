# Django import
from django.contrib import admin
# Local import
from players.models import InvitationTemplate


@admin.register(InvitationTemplate)
class InvitationTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template')
