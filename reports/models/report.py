# Python import
from datetime import datetime
# Django import
from django.contrib.auth import get_user_model
from django.db import models
# Third-Party import
from djchoices import DjangoChoices, ChoiceItem


class ReportTypesChoice(DjangoChoices):
    TEST = ChoiceItem('test')
    SCOUTING = ChoiceItem('scouting')


class Report(models.Model):
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reports")
    open_date = models.DateTimeField(default=datetime.now)
    close_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    type = models.CharField(max_length=8, choices=ReportTypesChoice.choices, default=ReportTypesChoice.SCOUTING)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return f'[#{str(self.id)} {self.title}]'
