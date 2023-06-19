# Local import
from otp_auth.policies import VerifiedAccessPolicy


class OrganizationApiKeyAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_organizationapikey'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_organizationapikey'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_organizationapikey'],
            "effect": "allow"
        },
        {
            "action": ["update", "update_partial"],
            "principal": ['permission:change_organizationapikey'],
            "effect": "allow"
        },
    ]
