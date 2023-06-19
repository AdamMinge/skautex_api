# Django import
from django.db import models
# Third-Party import
from djchoices import DjangoChoices, ChoiceItem
# Local import
from players.models import Player
from reports.models.report import Report


class PlayerReportStatusChoice(DjangoChoices):
    DONE = ChoiceItem('done')
    CLOSED = ChoiceItem('closed')
    TODO = ChoiceItem('todo')


class PlayerReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="player_reports")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_reports")
    description = models.CharField(max_length=512, blank=True, null=True)
    status = models.CharField(max_length=6, choices=PlayerReportStatusChoice.choices, default=PlayerReportStatusChoice.TODO)

    @property
    def score(self):
        scores = []
        for profile in self.profiles.all():
            for statistic in profile.statistics.all():
                scores.append(0 if statistic.value is None else statistic.value)
            for group in profile.groups.all():
                for statistic in group.statistics.all():
                    scores.append(0 if statistic.value is None else statistic.value)
        return sum(scores) / len(scores) if scores else 0

    class Meta:
        verbose_name = "Player Report"
        verbose_name_plural = "Player Reports"
