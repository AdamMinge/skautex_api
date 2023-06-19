# Python import
from random import randint
from datetime import datetime, timedelta
# Local import
from reports.models import (Report, ReportPermission, ReportPermissionChoice)
from accounts.tests import create_test_users


def __get_random(elements):
    return elements[randint(0, len(elements) - 1)]


def create_test_report():
    reports = dict()
    users = list(create_test_users().values())

    for nr in range(10):
        title = 'report{}'.format(nr)
        open_date = datetime.now()
        close_date = open_date + timedelta(days=randint(1, 30))
        descriptions = title + f' descriptions'

        reports[title], _ = Report.objects.get_or_create(
            title=title, owner=__get_random(users), open_date=open_date,
            close_date=close_date, description=descriptions)

    return reports


def create_test_report_permission():
    reports = list(create_test_report().values())
    users = list(create_test_users().values())
    report_permissions = [ReportPermissionChoice.EDITOR, ReportPermissionChoice.VIEWER]

    for report in reports:
        connected_users = set()
        for nr in range(0, 3):
            connected_users.add(__get_random(users))
        for connected_user in connected_users:
            if connected_user != report.owner:
                ReportPermission.objects.get_or_create(
                    report=report, user=connected_user, permission=__get_random(report_permissions))


def create_test_player_report():
    pass


def create_test_player_report_statistics():
    pass


def create_test_player_report_statistics_type():
    pass
