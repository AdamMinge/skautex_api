# Local import
from accounts.utils import get_all_permissions_for_user
from otp_auth.policies import VerifiedAccessPolicy


class AuditEntryAccessPolicy(VerifiedAccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": ['permission:view_auditentry', 'permission:view_own_auditentries'],
            "effect": "allow"
        },
    ]

    @classmethod
    def scope_queryset(cls, request, queryset):
        if 'view_auditentry' not in list(get_all_permissions_for_user(request.user).values_list('codename', flat=True)):
            queryset = queryset.filter(user=request.user)
        return queryset

