from otp_auth.views.jwt import JWTObtainView, JWTRefreshView
from otp_auth.views.organization import OrganizationViewSet
from otp_auth.views.organization_api_key import OrganizationApiKeyViewSet
from otp_auth.views.totp_device import TOTPDeviceView
from otp_auth.views.static_device import StaticDeviceView
from otp_auth.views.email_device import EmailDeviceView
from otp_auth.views.verification import DeviceVerifyView

__all__ = ['JWTObtainView', 'JWTRefreshView', 'OrganizationViewSet',
           'OrganizationApiKeyViewSet', 'TOTPDeviceView', 'DeviceVerifyView',
           'StaticDeviceView', 'EmailDeviceView']
