# Local import
from otp_auth.policies import VerifiedAccessPolicy


class InvitationTemplateAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", 'download'],
            "principal": ['permission:view_invitationtemplate'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_invitationtemplate'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_invitationtemplate'],
            "effect": "allow"
        },
    ]
