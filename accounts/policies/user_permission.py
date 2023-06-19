# Local import
from otp_auth.policies import VerifiedAccessPolicy
from accounts.utils import get_user_by_id


class UserPermissionAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list_update"],
            "principal": ['permission:change_user_permission'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["list"],
            "permissions":
                [
                    (['permission:view_user'], None),
                    (['permission:view_own_user'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    def is_own_user(self, request, view, action):
        return get_user_by_id(request=request, user_id=view.kwargs['user_id']) == request.user
