# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# Local import
from reports.models.player_report_profiles import PlayerReportProfiles
from reports.models.player_report_profile_statistics import PlayerReportProfileStatistics


class PlayerReportProfileStatisticsGroups(models.Model):
    name = models.CharField(max_length=512)
    profile = models.ForeignKey(PlayerReportProfiles, on_delete=models.CASCADE, related_name="groups")

    statistics = GenericRelation(PlayerReportProfileStatistics)

    class Meta:
        verbose_name = "Player Report Profile Statistics Group"
        verbose_name_plural = "Player Report Profile Statistics Groups"
        unique_together = ('name', 'profile',)

    def __str__(self):
        return f'[#{str(self.id)} {self.name}'
