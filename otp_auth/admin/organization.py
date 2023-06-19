# Django import
from django.contrib import admin
# Local import
from otp_auth.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')

