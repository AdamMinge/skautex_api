# Python import
import os
from xml.etree import ElementTree
# Django import
from django.contrib.contenttypes.models import ContentType
# Local import
from players.models import PlayerPositionChoice
from reports.models import (PlayerReport, PlayerReportProfiles, PlayerReportProfileStatistics,
                            PlayerReportProfileStatisticsGroups)


SCHEMA_DIR = os.path.dirname(os.path.abspath(__file__))


def __add_statistic(name, container):
    container_type = ContentType.objects.get_for_model(type(container))
    statistic = PlayerReportProfileStatistics.objects.create(
        name=name, content_type=container_type, object_id=container.id)
    return statistic


def __fill_profiles(schema_root, player_report):
    for profile in schema_root.iter('profile'):
        created_profile = PlayerReportProfiles.objects.create(name=profile.attrib['name'],
                                                              player_report=player_report)

        for group in profile.findall('group'):
            created_group = PlayerReportProfileStatisticsGroups.objects.create(name=group.attrib['name'],
                                                                               profile=created_profile)
            for statistic in group.findall('statistic'):
                __add_statistic(name=statistic.attrib['name'], container=created_group)

        for statistic in profile.findall('statistic'):
            __add_statistic(name=statistic.attrib['name'], container=created_profile)


def __create_profiles(player_report):
    profile_schema_for_position = {
        PlayerPositionChoice.GOALKEEPER_1: os.path.join(SCHEMA_DIR, 'profiles/goalkeeper.xml'),
        PlayerPositionChoice.SIDE_DEFENDER_2: os.path.join(SCHEMA_DIR, 'profiles/side_defender.xml'),
        PlayerPositionChoice.SIDE_DEFENDER_3: os.path.join(SCHEMA_DIR, 'profiles/side_defender.xml'),
        PlayerPositionChoice.CENTRAL_DEFENDER_4: os.path.join(SCHEMA_DIR, 'profiles/central_defender.xml'),
        PlayerPositionChoice.CENTRAL_DEFENDER_5: os.path.join(SCHEMA_DIR, 'profiles/central_defender.xml'),
        PlayerPositionChoice.DEFENSIVE_HELP_6: os.path.join(SCHEMA_DIR, 'profiles/defensive_help.xml'),
        PlayerPositionChoice.MIDDLE_HELP_8: os.path.join(SCHEMA_DIR, 'profiles/middle_help_8.xml'),
        PlayerPositionChoice.MIDDLE_HELP_10: os.path.join(SCHEMA_DIR, 'profiles/middle_help_10.xml'),
        PlayerPositionChoice.SIDE_HELP_7: os.path.join(SCHEMA_DIR, 'profiles/side_help.xml'),
        PlayerPositionChoice.SIDE_HELP_11: os.path.join(SCHEMA_DIR, 'profiles/side_help.xml'),
        PlayerPositionChoice.ATTACKER_9: os.path.join(SCHEMA_DIR, 'profiles/attacker.xml'),
    }

    profile_schema = profile_schema_for_position.get(player_report.player.position)
    if profile_schema:
        __fill_profiles(ElementTree.parse(profile_schema).getroot(), player_report)


def create_player_report(**kwargs):
    player_report = PlayerReport.objects.create(**kwargs)
    __create_profiles(player_report)
    return player_report
