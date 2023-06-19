# Django import
from django.db import models
# Local import
from booking.models.booking_objects_types import BookingObjectsTypes


class BookingObjects(models.Model):
    name = models.CharField(max_length=128)
    type = models.ForeignKey(BookingObjectsTypes, on_delete=models.CASCADE, related_name="booking_objects")

    class Meta:
        verbose_name = "Booking Object"
        verbose_name_plural = "Booking Objects"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
