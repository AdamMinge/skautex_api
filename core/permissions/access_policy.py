# Third-Party import
from rest_access_policy import AccessPolicy
# Local import
from accounts.utils import get_all_permissions_for_user


class BaseAccessPolicy(AccessPolicy):
    group_prefix = "permission:"
    extra_statements = []

    def get_user_group_values(self, user):
        return list(get_all_permissions_for_user(user).values_list('codename', flat=True))

    def get_policy_statements(self, request, view):
        new_statements = []
        for statement in self.extra_statements:
            for permission in statement['permissions']:
                new_statement = {
                    'action': statement['action'],
                    'effect': statement['effect'],
                    'principal': permission[0]
                }
                if permission[1] is not None:
                    new_statement['condition'] = permission[1]
                new_statements.append(new_statement)
        return self.statements + new_statements

    @classmethod
    def scope_queryset(cls, request, queryset):
        return queryset

    def _convert_statements_to_swagger(self, view, statements):
        action = self._get_invoked_action(view)
        swagger_statements = [statement['principal'] for statement in statements
                              if action in statement['action'] or '*' in statement['action']]
        swagger_statements = [item for sublist in swagger_statements for item in sublist]
        swagger_statements = [statement.split(':', 1)[1] for statement in swagger_statements
                              if ':' in statement]
        return swagger_statements

    def get_swagger_permissions(self, request, view):
        statements = self.get_policy_statements(request, view)
        statements = self._normalize_statements(statements)
        statements = self._convert_statements_to_swagger(view, statements)
        return statements





