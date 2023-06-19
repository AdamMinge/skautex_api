# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PlayerReportAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ['*'],
            "effect": "allow"
        },
    ]
