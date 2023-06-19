# Django import
from django.contrib import admin
# Local import
from calendars.models import EventsConnectedUsers


@admin.register(EventsConnectedUsers)
class EventsConnectedUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
