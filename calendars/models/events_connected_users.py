# Django import
from django.db import models
from django.contrib.auth import get_user_model
# Local import
from calendars.models.events import Events


class EventsConnectedUsers(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="event_connected_users")
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="event_connected_users")

    class Meta:
        verbose_name = "Event Connected User"
        verbose_name_plural = "Event Connected Users"
        unique_together = ('user', 'event',)
