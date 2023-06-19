# Django import
from django.db import models


class League(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = "League"
        verbose_name_plural = "Leagues"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
