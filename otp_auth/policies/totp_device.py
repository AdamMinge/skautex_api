# Local import
from accounts.utils import get_all_permissions_for_user
from core.utils import get_object_for_url
from otp_auth.policies import VerifiedAccessPolicy


class TOTPDeviceAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_totpdevice', 'permission:view_own_totpdevice'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["create"],
            "permissions":
                [
                    (['permission:add_totpdevice'], None),
                    (['permission:add_own_totpdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_totpdevice'], None),
                    (['permission:delete_own_totpdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_totpdevice'], None),
                    (['permission:change_own_totpdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_totpdevice' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

    def is_own_user(self, request, view, action):
        if action == 'create':
            user = get_object_for_url(request.data['user'])
            return user == request.data
        else:
            return view.get_object().user == request.data
