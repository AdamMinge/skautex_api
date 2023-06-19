# Global import
import typing
# Third-Party import
from rest_framework_api_key.models import BaseAPIKeyManager
from rest_framework_api_key.crypto import split


class OrganizationAPIKeyManager(BaseAPIKeyManager):
    def get_usable_keys(self):
        return super().get_usable_keys().filter(organization__active=True)

    def generate_key(self):
        try:
            key, prefix, hashed_key = self.key_generator.generate()
        except ValueError:
            generate = typing.cast(
                typing.Callable[[], typing.Tuple[str, str]], self.key_generator.generate
            )
            key, hashed_key = generate()
            prefix, hashed_key = split(hashed_key)

        return key, prefix, hashed_key,

    def assign_key(self, obj):
        key, obj.prefix, obj.hashed_key = self.generate_key()
        return key
