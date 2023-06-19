# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from calendars.models import EventsConnectedUsers, Events


class EventsConnectedUsersFilter(filters.FilterSet):
    event = filters.ModelChoiceFilter(field_name='owner', queryset=Events.objects.all())
    user = filters.ModelChoiceFilter(field_name='owner', queryset=get_user_model().objects.all())

    class Meta:
        model = EventsConnectedUsers
        fields = []
