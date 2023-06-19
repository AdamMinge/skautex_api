# Django import
from django.utils.translation import gettext as _
# Third-Party import
from rest_framework_simplejwt import tokens


class CustomizableBlackListMixin:
    if 'rest_framework_simplejwt.token_blacklist' in tokens.settings.INSTALLED_APPS:
        def verify(self, *args, **kwargs):
            self.check_blacklist()
            super().verify(*args, **kwargs)

        def check_blacklist(self):
            jti = self.payload[tokens.api_settings.JTI_CLAIM]
            if tokens.BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise tokens.TokenError(_('Token is blacklisted'))

        def blacklist(self):
            jti = self.payload[tokens.api_settings.JTI_CLAIM]
            exp = self.payload['exp']
            token, _ = tokens.OutstandingToken.objects.get_or_create(
                jti=jti,
                defaults={
                    'token': str(self),
                    'expires_at': tokens.datetime_from_epoch(exp),
                },
            )
            return tokens.BlacklistedToken.objects.get_or_create(token=token)

    @classmethod
    def for_user(cls, user, token_claims=None):
        token = super().for_user(user)

        if token_claims is not None:
            for claim, value in token_claims.items():
                if claim not in token:
                    token[claim] = value

        jti = token[tokens.api_settings.JTI_CLAIM]
        exp = token['exp']

        tokens.OutstandingToken.objects.create(
            user=user,
            jti=jti,
            token=str(token),
            created_at=token.current_time,
            expires_at=tokens.datetime_from_epoch(exp),
        )

        return token


class CustomizableRefreshToken(CustomizableBlackListMixin, tokens.Token):
    token_type = 'refresh'
    lifetime = tokens.api_settings.REFRESH_TOKEN_LIFETIME
    no_copy_claims = (
        tokens.api_settings.TOKEN_TYPE_CLAIM,
        'exp',
        tokens.api_settings.JTI_CLAIM,
        'jti',
    )

    @property
    def access_token(self):
        access = tokens.AccessToken()
        access.set_exp(from_time=self.current_time)
        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value
        return access


def create_refresh_token(user, device=None):
    custom_token_claims = dict()

    if (user is not None) and (device is not None) and (device.user_id == user.id) and (device.confirmed is True):
        custom_token_claims['otp_device_id'] = device.persistent_id
    else:
        custom_token_claims['otp_device_id'] = None

    token = CustomizableRefreshToken.for_user(user, custom_token_claims)
    return token
