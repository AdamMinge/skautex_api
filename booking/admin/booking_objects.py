# Django import
from django.contrib import admin
# Local import
from booking.models import BookingObjects


@admin.register(BookingObjects)
class BookingObjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
