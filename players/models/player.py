# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# Third-Party import
from djchoices import DjangoChoices, ChoiceItem
# Local import
from core.backends.azure_storage import AzureMediaStorage
from contact_details.models import ContactDetail
from players.models.team import Team
from players.models.league import League
from players.utils import create_player_profile_picture_path


class PlayerPositionChoice(DjangoChoices):
    GOALKEEPER_1 = ChoiceItem('goalkeeper 1')
    SIDE_DEFENDER_2 = ChoiceItem('side defender 2')
    SIDE_DEFENDER_3 = ChoiceItem('side defender 3')
    CENTRAL_DEFENDER_4 = ChoiceItem('central defender 4')
    CENTRAL_DEFENDER_5 = ChoiceItem('central defender 5')
    DEFENSIVE_HELP_6 = ChoiceItem('defensive help 6')
    MIDDLE_HELP_8 = ChoiceItem('middle help 8')
    MIDDLE_HELP_10 = ChoiceItem('middle help 10')
    SIDE_HELP_7 = ChoiceItem('side help 7')
    SIDE_HELP_11 = ChoiceItem('side help 11')
    ATTACKER_9 = ChoiceItem('attacker 9')


class PlayerStatusChoice(DjangoChoices):
    OBSERVATION = ChoiceItem('observation')
    INAPPROPRIATE = ChoiceItem('inappropriate')
    TEST = ChoiceItem('test')
    FOR_TESTING = ChoiceItem('for testing')


class PlayerDominantLegChoice(DjangoChoices):
    LEFT = ChoiceItem('left')
    RIGHT = ChoiceItem('right')
    NONE = ChoiceItem('none')


class Player(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    position = models.CharField(max_length=18, choices=PlayerPositionChoice.choices)
    birth_date = models.DateField()
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    dominant_leg = models.CharField(max_length=5, choices=PlayerDominantLegChoice.choices, default=PlayerDominantLegChoice.NONE)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(storage=AzureMediaStorage(), upload_to=create_player_profile_picture_path, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="players")
    status = models.CharField(max_length=13, choices=PlayerStatusChoice.choices, default=PlayerStatusChoice.OBSERVATION)

    contact_details = GenericRelation(ContactDetail)

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return f'[#{str(self.id)} {self.name} {self.surname}]'
