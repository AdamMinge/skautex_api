# Django import
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
