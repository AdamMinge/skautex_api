# Local import
from otp_auth.policies import VerifiedAccessPolicy


class OrganizationAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_organization'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_organization'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_organization'],
            "effect": "allow"
        },
        {
            "action": ["update", "update_partial"],
            "principal": ['permission:change_organization'],
            "effect": "allow"
        },
    ]
