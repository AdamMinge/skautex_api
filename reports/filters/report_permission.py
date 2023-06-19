# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
# Local import
from reports.models import Report, ReportPermission


class ReportPermissionFilter(filters.FilterSet):
    report = filters.ModelChoiceFilter(field_name='report', queryset=Report.objects.all())
    user = filters.ModelChoiceFilter(field_name='user', queryset=get_user_model().objects.all())
    permission = filters.AutoFilter(lookups=['exact'], field_name='permission')

    order = filters.OrderingFilter(fields={'report__title': 'report', 'user__username': 'user',
                                           'permission': 'permission'})

    class Meta:
        model = ReportPermission
        fields = []
