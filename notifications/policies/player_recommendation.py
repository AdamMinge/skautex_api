# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PlayerRecommendationAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ['*'],
            "effect": "allow"
        },
    ]