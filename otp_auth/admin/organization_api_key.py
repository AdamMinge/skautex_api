# Django import
from django.contrib import admin
# Third-Party import
from rest_framework_api_key.admin import APIKeyModelAdmin
from rest_framework_api_key.models import APIKey
# Local import
from otp_auth.models import OrganizationAPIKey


@admin.register(OrganizationAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    list_display = [*APIKeyModelAdmin.list_display, 'get_organization_name']

    def get_organization_name(self, obj):
        return obj.organization.name
    get_organization_name.admin_order_field = 'organization'
    get_organization_name.short_description = 'Organization'


admin.site.unregister(APIKey)
