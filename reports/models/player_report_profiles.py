# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# Local import
from reports.models.player_report import PlayerReport
from reports.models.player_report_profile_statistics import PlayerReportProfileStatistics


class PlayerReportProfiles(models.Model):
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=512, blank=True, null=True)
    player_report = models.ForeignKey(PlayerReport, on_delete=models.CASCADE, related_name="profiles")

    statistics = GenericRelation(PlayerReportProfileStatistics)

    class Meta:
        verbose_name = "Player Report Profile"
        verbose_name_plural = "Player Report Profiles"
        unique_together = ('name', 'player_report',)

    def __str__(self):
        return f'[#{str(self.id)} {self.name}'
