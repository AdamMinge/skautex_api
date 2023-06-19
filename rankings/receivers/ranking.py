# Django Import
from django.dispatch import receiver
from django.db.models.signals import post_save
# Local Import
from players.models import Player
from reports.models import PlayerReportProfileStatistics, PlayerReportProfileStatisticsGroups, PlayerReport
from rankings.models import Ranking


@receiver(post_save, sender=Player)
def created_player(sender, instance, created, **kwargs):
    if created:
        Ranking.objects.create(player=instance, score=0)


def __get_player_report_for_statistic(statistic):
    if type(statistic.content_object) == PlayerReportProfileStatisticsGroups:
        return statistic.content_object.profile.player_report
    else:
        return statistic.content_object.player_report


@receiver(post_save, sender=PlayerReportProfileStatistics)
def update_statistic(sender, instance, created, **kwargs):
    updated_player_report = __get_player_report_for_statistic(instance)

    ranking = Ranking.objects.filter(player=updated_player_report.player).first()
    if ranking:
        player_reports = PlayerReport.objects.filter(player=updated_player_report.player).all()

        player_reports_count = len(player_reports) + 1 if created else len(player_reports)
        ranking.score = sum(player_report.score for player_report in player_reports) / player_reports_count
        ranking.save()
