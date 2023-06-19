# Local import
from otp_auth.policies import VerifiedAccessPolicy


class UserAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": ['permission:view_user'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_user'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["retrieve"],
            "permissions":
                [
                    (['permission:view_user'], None),
                    (['permission:view_own_user'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_user'], None),
                    (['permission:delete_own_user'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update", "update_password"],
            "permissions":
                [
                    (['permission:change_user'], None),
                    (['permission:change_own_user'], 'is_own_user')
                ],
            "effect": "allow"
        },
        {
            "action": ["upload_file"],
            "permissions":
                [
                    (['permission:change_user'], None),
                    (['permission:change_own_user'], 'is_own_user')
                ],
            "effect": "allow"
        },
    ]

    def is_own_user(self, request, view, action):
        return request.user == view.get_object()
