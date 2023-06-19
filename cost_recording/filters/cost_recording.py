# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from cost_recording.models import CostRecording


class CostRecordingFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    money = filters.AutoFilter(lookups=['exact', 'contains'], field_name='money')
    record_date = filters.IsoDateTimeFilter(field_name='record_date')
    owner = filters.ModelChoiceFilter(field_name='owner', queryset=get_user_model().objects.all())

    order = filters.OrderingFilter(fields={'name': 'name', 'money': 'money',
                                           'record_date': 'record_date', 'owner__username': 'owner', })

    class Meta:
        model = CostRecording
        fields = []


