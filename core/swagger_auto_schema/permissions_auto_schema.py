# Python import
from typing import List
from collections import namedtuple
# Third-Party import
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.permissions import OperandHolder, SingleOperandHolder


PermissionItem = namedtuple('PermissionItem', ['name'])


def _render_permission_item(item):
    return f'+ `{item.name}` \n'


class PermissionsAutoSchema(SwaggerAutoSchema):
    def get_summary_and_description(self):
        summary, description = super().get_summary_and_description()
        permissions_description = self._get_permissions_description()
        if permissions_description:
            description += permissions_description

        return summary, description

    def _handle_permission(self, permission_class):
        permissions = []

        try:
            permissions_docs = permission_class().get_swagger_permissions(self.request, self.view)
        except AttributeError:
            return []

        for permissions_doc in permissions_docs:
            permissions.append(PermissionItem(permissions_doc))

        return permissions

    def _gather_permissions(self) -> List[PermissionItem]:
        items = []

        for permission_class in getattr(self.view, 'permission_classes', []):
            if isinstance(permission_class, OperandHolder):
                items.extend(
                    self._handle_permission(permission_class.op1_class))
                items.extend(
                    self._handle_permission(permission_class.op2_class))

            if isinstance(permission_class, SingleOperandHolder):
                items.extend(
                    self._handle_permission(permission_class.op1_class))

            items.extend(self._handle_permission(permission_class))

        return [i for i in items if i]

    def _get_permissions_description(self):
        permission_items = self._gather_permissions()

        if permission_items:
            return '\n\n**Permissions:**\n' + '\n'.join(
                _render_permission_item(item) for item in permission_items
            )
        else:
            return None
