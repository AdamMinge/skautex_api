# Local import
from accounts.utils import get_all_permissions_for_user
from otp_auth.policies import VerifiedAccessPolicy


class EventsConnectedUsersAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": ['permission:view_events', 'permission:view_own_events'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["retrieve"],
            "permissions":
                [
                    (['permission:view_events'], None),
                    (['permission:view_own_events'], 'is_own_event')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update", "create", "destroy"],
            "permissions":
                [
                    (['permission:change_events'], None),
                    (['permission:change_own_events'], 'is_own_event')
                ],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_events' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

    def is_own_event(self, request, view, action):
        return view.get_object().event.user == request.user
