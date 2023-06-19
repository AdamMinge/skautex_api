# Local import
from otp_auth.policies import AuthenticatedAccessPolicy


class DeviceVerifyAccessPolicy(AuthenticatedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]