# Local import
from otp_auth.policies import VerifiedAccessPolicy


class ReportPermissionAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ['*'],
            "effect": "allow"
        },
    ]
