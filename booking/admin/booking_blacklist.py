# Django import
from django.contrib import admin
# Local import
from booking.models import BookingBlacklist


@admin.register(BookingBlacklist)
class BookingBlacklistAdmin(admin.ModelAdmin):
    list_display = ('booking_object', 'user', 'description')
