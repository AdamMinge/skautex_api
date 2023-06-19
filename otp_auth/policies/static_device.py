# Local import
from accounts.utils import get_all_permissions_for_user
from core.utils import get_object_for_url
from otp_auth.policies import VerifiedAccessPolicy


class StaticDeviceAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_staticdevice', 'permission:view_own_staticdevice'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["create"],
            "permissions":
                [
                    (['permission:add_staticdevice'], None),
                    (['permission:add_own_staticdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_staticdevice'], None),
                    (['permission:delete_own_staticdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_staticdevice'], None),
                    (['permission:change_own_staticdevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_staticdevice' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

    def is_own_user(self, request, view, action):
        if action == 'create':
            user = get_object_for_url(request.data['user'])
            return user == request.data
        else:
            return view.get_object().user == request.data
