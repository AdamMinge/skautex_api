# Local import
from otp_auth.policies import APIKeyAccessPolicy


class JWTObtainAccessPolicy(APIKeyAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]


class JWTRefreshAccessPolicy(APIKeyAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]
