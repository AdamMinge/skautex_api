# Third-Party import
import rest_framework_filters as filters
# Local import
from accounts.models import AuditEntry
from accounts.models import User


class AuditEntryFilter(filters.FilterSet):
    ip = filters.AutoFilter(lookups=['exact', 'contains'], field_name='ip')
    logged_date = filters.IsoDateTimeFilter(field_name='logged_date')
    user = filters.ModelChoiceFilter(field_name='user', queryset=User.objects.all())

    order = filters.OrderingFilter(fields={'ip': 'ip', 'logged_date': 'logged_date', 'user__username': 'user'})

    class Meta:
        model = AuditEntry
        fields = []
