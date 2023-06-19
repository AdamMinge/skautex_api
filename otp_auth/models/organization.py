# Django import
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return f'[#{str(self.id)} {self.name}]'
