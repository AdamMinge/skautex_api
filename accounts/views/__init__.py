from accounts.views.group import GroupViewSet
from accounts.views.permission import PermissionViewSet
from accounts.views.user import UserViewSet
from accounts.views.audit_entry import AuditEntryViewSet
from accounts.views.user_all_permission import UserAllPermissionViewSet
from accounts.views.user_group import UserGroupViewSet
from accounts.views.user_permission import UserPermissionViewSet
from accounts.views.user_contact_detail import UserContactDetailViewSet

__all__ = ['GroupViewSet', 'UserViewSet', 'AuditEntryViewSet', 'PermissionViewSet', 'UserAllPermissionViewSet',
           'UserGroupViewSet', 'UserPermissionViewSet', 'UserContactDetailViewSet']
