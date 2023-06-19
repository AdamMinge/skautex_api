# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PlayerReportFileAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ['*'],
            "effect": "allow"
        },
    ]
