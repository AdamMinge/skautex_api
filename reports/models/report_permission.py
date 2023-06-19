# Django import
from django.contrib.auth import get_user_model
from django.db import models
# Third-Party import
from djchoices import DjangoChoices, ChoiceItem
# Local import
from reports.models.report import Report


class ReportPermissionChoice(DjangoChoices):
    EDITOR = ChoiceItem('editor')
    VIEWER = ChoiceItem('viewer')


class ReportPermission(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="permissions")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="permissions")
    permission = models.CharField(max_length=30, choices=ReportPermissionChoice.choices)

    class Meta:
        verbose_name = "Report Permission"
        verbose_name_plural = "Report Permissions"
