# Django import
from django.contrib.auth import get_user_model
# Third-Party import
import rest_framework_filters as filters
from django_otp.plugins.otp_totp.models import TOTPDevice


class TOTPDeviceFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=['exact', 'contains'], field_name='name')
    confirmed = filters.AutoFilter(lookups=['exact'], field_name='confirmed')
    user = filters.ModelChoiceFilter(field_name='user', queryset=get_user_model().objects.all())

    order = filters.OrderingFilter(fields={'name': 'name',
                                           'confirmed': 'confirmed',
                                           'user__username': 'user'})

    class Meta:
        model = TOTPDevice
        fields = []

