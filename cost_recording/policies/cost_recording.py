# Local import
from otp_auth.policies import VerifiedAccessPolicy


class CostRecordingAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_costrecording'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_costrecording'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_costrecording'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_costrecording'],
            "effect": "allow"
        },
    ]
