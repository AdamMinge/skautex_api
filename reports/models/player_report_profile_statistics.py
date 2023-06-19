# Django import
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PlayerReportProfileStatistics(models.Model):
    name = models.CharField(max_length=512)
    value = models.IntegerField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "Player Report Profile Statistics"
        verbose_name_plural = "Player Report Profile Statistics"
        unique_together = ('name', 'content_type', 'object_id',)

    def __str__(self):
        return f'[#{str(self.id)} {self.name}'
