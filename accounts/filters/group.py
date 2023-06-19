# Django import
from django.contrib.auth.models import Group
# Third-Party import
import rest_framework_filters as filters


class GroupFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    order = filters.OrderingFilter(fields=['name'])

    class Meta:
        model = Group
        fields = []
