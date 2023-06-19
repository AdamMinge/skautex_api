# Django import
from django.db import models


class EventsTypes(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = "Event Type"
        verbose_name_plural = "Events Types"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
