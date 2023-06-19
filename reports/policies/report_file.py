# Local import
from otp_auth.policies import VerifiedAccessPolicy


class ReportFileAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ['*'],
            "effect": "allow"
        },
    ]
