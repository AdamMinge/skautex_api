# Django import
from django.contrib import admin
# Local import
from linked_files.models import LinkedFile


@admin.register(LinkedFile)
class LinkedFileAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'file')
