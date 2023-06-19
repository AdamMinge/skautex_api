# Django import
from django.db import models
from django.contrib.auth import get_user_model
# Local import
from booking.models.booking_objects import BookingObjects


class BookingReservations(models.Model):
    booking_object = models.ForeignKey(BookingObjects, on_delete=models.CASCADE, related_name="booking_reservations")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="booking_reservations")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Booking Reservation"
        verbose_name_plural = "Booking Reservations"
