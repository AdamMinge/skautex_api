# Local import
from otp_auth.policies import VerifiedAccessPolicy


class GroupAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_group'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_group'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_group'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_group'],
            "effect": "allow"
        },
    ]
