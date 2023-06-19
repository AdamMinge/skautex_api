# Django import
from django.contrib.auth.models import Permission
# Third-Party import
import rest_framework_filters as filters


class PermissionFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')

    order = filters.OrderingFilter(fields=['name'])

    class Meta:
        model = Permission
        fields = []
