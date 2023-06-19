# Third-Party import
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import HTTP_HEADER_ENCODING, AUTH_HEADER_TYPE_BYTES
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from django_otp.models import Device


class Verified(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        header = self.get_header(request)
        if header is None:
            return False
        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return False
        validated_token = self.get_validated_token(raw_token)
        if validated_token is None:
            return False
        persistent_id = validated_token.get('otp_device_id')
        if persistent_id is not None:
            device = Device.from_persistent_id(persistent_id)
            return not ((device is not None) and (device.user_id != request.user.id))
        return False

    def get_header(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')
        if isinstance(header, str):
            header = header.encode(HTTP_HEADER_ENCODING)
        return header

    def get_raw_token(self, header):
        parts = header.split()
        if len(parts) == 0:
            return None
        if parts[0] not in AUTH_HEADER_TYPE_BYTES:
            return None
        if len(parts) != 2:
            return None
        return parts[1]

    def get_validated_token(self, raw_token):
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError:
                return None
        return None
