# Django import
from django.db import models
from django.contrib.auth import get_user_model
# Local import
from booking.models.booking_objects import BookingObjects


class BookingBlacklist(models.Model):
    booking_object = models.ForeignKey(BookingObjects, on_delete=models.CASCADE, related_name="booking_blacklist")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="booking_blacklist")
    description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = "Booking Blacklist"
        verbose_name_plural = "Booking Blacklist"
        unique_together = ('booking_object', 'user',)
