# Django import
from django.db import models


class BookingObjectsTypes(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = "Booking Object Type"
        verbose_name_plural = "Booking Objects Types"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
