# Local import
from otp_auth.policies import VerifiedAccessPolicy


class InvitationAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "download"],
            "principal": ['permission:view_invitation'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_invitation'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_invitation'],
            "effect": "allow"
        },
    ]
