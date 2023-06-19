# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PermissionAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_permission'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_permission'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_permission'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_permission'],
            "effect": "allow"
        },
    ]
