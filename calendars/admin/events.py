# Django import
from django.contrib import admin
# Local import
from calendars.models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'status',
                    'end_date', 'owner', 'type', 'hide', 'color')
