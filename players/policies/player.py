# Local import
from otp_auth.policies import VerifiedAccessPolicy


class PlayerAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_player'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_player'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_player'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_player'],
            "effect": "allow"
        },
        {
            "action": ["upload_file"],
            "principal": ['permission:change_player'],
            "effect": "allow"
        },
    ]
