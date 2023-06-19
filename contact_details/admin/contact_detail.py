# Django import
from django.contrib import admin
# Local import
from contact_details.models import ContactDetail


@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'type', 'value')
