# Local import
from otp_auth.policies import VerifiedAccessPolicy


class LeagueAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_league'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_league'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_league'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_league'],
            "effect": "allow"
        },
    ]
