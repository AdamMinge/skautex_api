# Django import
from django.contrib import admin
# Local import
from cost_recording.models import CostRecording


@admin.register(CostRecording)
class CostRecordingAdmin(admin.ModelAdmin):
    list_display = ('name', 'money', 'record_date', 'owner')
