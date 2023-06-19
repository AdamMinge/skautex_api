# Local import
from accounts.utils import get_all_permissions_for_user
from otp_auth.policies import VerifiedAccessPolicy
from reports.models import ReportPermission, ReportPermissionChoice


class ReportAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list"],
            "principal": ['permission:view_report', 'permission:view_own_report'],
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ['permission:add_report'],
            "effect": "allow"
        },
    ]
    extra_statements = [
        {
            "action": ["retrieve"],
            "permissions":
                [
                    (['permission:view_report'], None),
                    (['permission:view_own_report'], 'has_viewer_permissions')
                ],
            "effect": "allow"
        },
        {
            "action": ["destroy"],
            "permissions":
                [
                    (['permission:delete_report'], None),
                    (['permission:delete_own_report'], 'has_owner_permissions')
                ],
            "effect": "allow"
        },
        {
            "action": ["update", "partial_update"],
            "permissions":
                [
                    (['permission:change_report'], None),
                    (['permission:change_own_report'], 'has_editor_permissions')
                ],
            "effect": "allow"
        },
        {
            "action": ["download"],
            "permissions":
            [
                (['permission:view_report'], None),
                (['permission:view_own_report'], 'has_viewer_permissions')
            ],
            "effect": "allow"
        }
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_report' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(owner=request.user)
        return queryset

    def has_owner_permissions(self, request, view, action):
        return request.user == view.get_object().owner

    def has_editor_permissions(self, request, view, action):
        return self.has_owner_permissions(request, view, action) | \
               self.__has_permission(request.user, view.get_object(), ReportPermissionChoice.EDITOR)

    def has_viewer_permissions(self, request, view, action):
        return self.has_editor_permissions(request, view, action) | \
               self.__has_permission(request.user, view.get_object(), ReportPermissionChoice.VIEWER)

    def __has_permission(self, user, report, permission):
        return ReportPermission.objects.filter(report=report, user=user, permission=permission).exists()
