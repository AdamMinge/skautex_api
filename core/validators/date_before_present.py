# Python import
from datetime import datetime
# Django import
from django.utils.translation import ugettext_lazy as _
# Third-Party import
from rest_framework import serializers
from rest_framework.utils.representation import smart_repr


class DateBeforePresentValidator:
    message = _('{date_field} should be before present.')

    def __init__(self, date_field="date", message=None):
        self.date_field = date_field
        self.message = message or self.message

    def __call__(self, attrs):
        if attrs[self.date_field] > datetime.now().date():
            message = self.message.format(date_field=self.date_field)
            raise serializers.ValidationError(message, code='date_before_present')

    def __repr__(self):
        return '<%s(date_field=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.date_field)
        )
