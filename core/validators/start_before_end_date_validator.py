# Django import
from django.utils.translation import ugettext_lazy as _
# Third-Party import
from rest_framework import serializers
from rest_framework.utils.representation import smart_repr


class StartBeforeEndDateValidator:
    message = _('{start_date_field} should be before {end_date_field}.')

    def __init__(self, start_date_field="start_date", end_date_field="end_date", message=None):
        self.start_date_field = start_date_field
        self.end_date_field = end_date_field
        self.message = message or self.message

    def __call__(self, attrs):
        if attrs[self.start_date_field] > attrs[self.end_date_field]:
            message = self.message.format(
                start_date_field=self.start_date_field,
                end_date_field=self.end_date_field,
            )
            raise serializers.ValidationError(message, code='start_before_end_date')

    def __repr__(self):
        return '<%s(start_date_field=%s, end_date_field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.start_date_field),
            smart_repr(self.end_date_field)
        )
