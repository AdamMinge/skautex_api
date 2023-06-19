# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PlayerContactDetailAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_player'],
            "effect": "allow"
        },
        {
            "action": ["destroy", "create", "update", "partial_update"],
            "principal": ['permission:change_player'],
            "effect": "allow"
        },
    ]
