# Django import
from django.apps import AppConfig


class RankingsConfig(AppConfig):
    name = 'rankings'

    def ready(self):
        from rankings import receivers
