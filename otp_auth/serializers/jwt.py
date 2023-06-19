# Third-Party import
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from otp_auth.utils import create_refresh_token, get_user_totp_devices, user_first_verification


class JWTObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return create_refresh_token(user)

    def validate(self, attrs):
        data = super().validate(attrs)
        if user_first_verification(self.user):
            otpauth_for_devices = {}
            for device_totp in get_user_totp_devices(self.user):
                otpauth_for_devices[device_totp.name] = device_totp.config_url
            data['otpauth'] = otpauth_for_devices
        return data


class JWTRefreshSerializer(TokenRefreshSerializer):
    pass
