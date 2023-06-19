# Django import
from django.contrib import admin
# Local import
from calendars.models import EventsTypes


@admin.register(EventsTypes)
class EventsTypesAdmin(admin.ModelAdmin):
    list_display = ('name', )
