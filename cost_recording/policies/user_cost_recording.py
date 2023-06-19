# Local import
from otp_auth.policies import VerifiedAccessPolicy
from accounts.utils import get_user_by_id


class UserCostRecordingAccessPolicy(VerifiedAccessPolicy):
    extra_statements = [
        {
            "action": ["create"],
            "permissions":
                [
                    (['permission:add_costrecording'], None),
                    (['permission:add_own_costrecording'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["retrieve", "list"],
            "permissions":
                [
                    (['permission:view_costrecording'], None),
                    (['permission:view_own_costrecording'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_costrecording'], None),
                    (['permission:delete_own_costrecording'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_costrecording'], None),
                    (['permission:change_own_costrecording'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    def is_own_user(self, request, view, action):
        return get_user_by_id(request=request, user_id=view.kwargs['user_id']) == request.user
