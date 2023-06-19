# Django import
from django.contrib.auth.models import Group
# Third-Party import
import rest_framework_filters as filters
# Local import
from accounts.models import User


class UserFilter(filters.FilterSet):
    username = filters.AutoFilter(lookups=['exact', 'contains'], field_name='username')
    first_name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='first_name')
    last_name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='last_name')
    email = filters.AutoFilter(lookups=['exact', 'contains'], field_name='email')
    is_active = filters.AutoFilter(lookups=['exact'], field_name='is_active')

    order = filters.OrderingFilter(fields=['first_name', 'username', 'last_name', 'email', 'is_active'])

    class Meta:
        model = User
        fields = []
