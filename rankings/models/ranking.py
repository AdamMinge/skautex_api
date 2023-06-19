# Django import
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Local import
from players.models import Player


class Ranking(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="ranking")
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    class Meta:
        verbose_name = "Ranking"
        verbose_name_plural = "Rankings"
