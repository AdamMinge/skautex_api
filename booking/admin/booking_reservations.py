# Django import
from django.contrib import admin
# Local import
from booking.models import BookingReservations


@admin.register(BookingReservations)
class BookingReservationsAdmin(admin.ModelAdmin):
    list_display = ('booking_object', 'user', 'start_date', 'end_date')
