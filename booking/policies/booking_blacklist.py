# Local import
from otp_auth.policies import VerifiedAccessPolicy


class BookingBlacklistAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_bookingblacklist'],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "principal": ['permission:delete_bookingblacklist'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_bookingblacklist'],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "principal": ['permission:change_bookingblacklist'],
            "effect": "allow"
        },
    ]
