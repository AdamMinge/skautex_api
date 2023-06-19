# Local import
from otp_auth.policies import VerifiedAccessPolicy


class CostRecordingFileAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:change_costrecording'],
            "effect": "allow"
        },
        {
            "action": ["destroy", "create", "update", "partial_update"],
            "principal": ['permission:change_costrecording'],
            "effect": "allow"
        },
    ]
