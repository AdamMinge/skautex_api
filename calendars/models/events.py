# Django import
from django.db import models
from django.contrib.auth import get_user_model
# Third-Party import
from colorfield.fields import ColorField
from djchoices import DjangoChoices, ChoiceItem
# Local import
from calendars.models.events_types import EventsTypes


class EventsStatus(DjangoChoices):
    TODO = ChoiceItem('todo')
    DONE = ChoiceItem('done')
    NONE = ChoiceItem('none')


class Events(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="events")
    type = models.ForeignKey(EventsTypes, on_delete=models.CASCADE, related_name="events")
    hide = models.BooleanField(default=False)
    color = ColorField(default='#0000FF')
    status = models.CharField(max_length=4, choices=EventsStatus.choices, default=EventsStatus.NONE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
