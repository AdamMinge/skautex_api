# Python import
from datetime import datetime
# Django import
from django.conf import settings
from django.db import models
# Third-Party import
from djmoney.models.fields import MoneyField


class CostRecording(models.Model):
    name = models.CharField(max_length=128)
    money = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='PLN')
    record_date = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cost_recording")

    class Meta:
        verbose_name = "Cost Recording"
        verbose_name_plural = "Cost Recording"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
