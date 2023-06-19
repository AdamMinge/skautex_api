# Local import
from otp_auth.policies import VerifiedAccessPolicy


class EventsTypesAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_eventstypes'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_eventstypes'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_eventstypes'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_eventstypes'],
            "effect": "allow"
        },
    ]
