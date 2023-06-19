# Django import
from django.core.management.base import BaseCommand
# Local import
from players.tests import create_test_teams, create_test_leagues, create_test_players


class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        create_test_teams()
        create_test_leagues()
        create_test_players()
