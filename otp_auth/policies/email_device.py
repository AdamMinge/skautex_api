# Local import
from accounts.utils import get_all_permissions_for_user
from core.utils import get_object_for_url
from otp_auth.policies import AuthenticatedAccessPolicy, VerifiedAccessPolicy


class EmailDeviceAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_emaildevice', 'permission:view_own_emaildevice'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["create"],
            "permissions":
                [
                    (['permission:add_emaildevice'], None),
                    (['permission:add_own_emaildevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_emaildevice'], None),
                    (['permission:delete_own_emaildevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_emaildevice'], None),
                    (['permission:change_own_emaildevice'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_emaildevice' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

    def is_own_user(self, request, view, action):
        if action == 'create':
            user = get_object_for_url(request.data['user'])
            return user == request.data
        else:
            return view.get_object().user == request.data


class EmailDeviceSendTokenAccessPolicy(AuthenticatedAccessPolicy):
    statements = [
        {
            "action": ["send_token_to_emails"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]
