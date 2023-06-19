# Local import
from otp_auth.policies import VerifiedAccessPolicy


class BookingObjectsAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_bookingobjects'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_bookingobjects'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_bookingobjects'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_bookingobjects'],
            "effect": "allow"
        },
    ]
