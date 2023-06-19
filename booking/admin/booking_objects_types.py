# Django import
from django.contrib import admin
# Local import
from booking.models import BookingObjectsTypes


@admin.register(BookingObjectsTypes)
class BookingObjectsTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
