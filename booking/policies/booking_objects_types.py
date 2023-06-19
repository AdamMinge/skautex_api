# Local import
from otp_auth.policies import VerifiedAccessPolicy


class BookingObjectsTypesAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_bookingobjectstypes'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_bookingobjectstypes'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_bookingobjectstypes'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_bookingobjectstypes'],
            "effect": "allow"
        },
    ]
