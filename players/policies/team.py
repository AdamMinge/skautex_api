# Local import
from otp_auth.policies import VerifiedAccessPolicy


class TeamAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_team'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_team'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_team'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_team'],
            "effect": "allow"
        },
    ]
