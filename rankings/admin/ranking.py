# Django import
from django.contrib import admin
# Local import
from rankings.models import Ranking


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('player', 'score')
