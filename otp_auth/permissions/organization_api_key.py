# Third-Party import
from rest_framework_api_key.permissions import BaseHasAPIKey
# Local import
from otp_auth.models import OrganizationAPIKey


class HasOrganizationAPIKey(BaseHasAPIKey):
    model = OrganizationAPIKey
