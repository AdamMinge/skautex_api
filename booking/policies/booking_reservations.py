# Local import
from accounts.utils import get_all_permissions_for_user
from otp_auth.policies import VerifiedAccessPolicy
from booking.models.booking_blacklist import BookingBlacklist


class BookingReservationsAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": ['permission:view_bookingreservations', 'permission:view_own_bookingreservations'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_own_bookingreservations', 'is_able_to_reservate'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["retrieve"],
            "permissions":
                [
                    (['permission:view_bookingreservations'], None),
                    (['permission:view_own_bookingreservations'], 'is_own_reservation')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_bookingreservations'], None),
                    (['permission:delete_own_bookingreservations'], 'is_own_reservation')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_bookingreservations'], None),
                    (['permission:change_own_bookingreservations'], 'is_own_reservation')
                ],
            "effect": "allow"
        },
        {
            "action": ["upload_file"],
            "permissions":
                [
                    (['permission:change_bookingreservations'], None),
                    (['permission:change_own_bookingreservations'], 'is_own_reservation')
                ],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_bookingreservations' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

    def is_own_reservation(self, request, view, action):
        return request.user == view.get_object().user

    def is_able_to_reservate(self, request, view, action):
        pass
