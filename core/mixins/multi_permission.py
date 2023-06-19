class MultiPermissionViewSetMixin(object):
    def get_permissions(self):
        """
        Look for permission class in self.permission_action_classes, which
        should be a dict mapping action name (key) to permissions class list (value),
        i.e.:

        class MyViewSet(MultiPermissionViewSetMixin, ViewSet):
            permission_class = MyDefaultSerializer
            permission_action_classes = {
               'list': [MyListPermissions1, MyListPermissions2],
               'my_action': [MyActionPermissions1],
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_permissions lookup: self.permission_classes, DefaultPermissions.

        """
        try:
            return [permission() for permission in self.permission_action_classes[self.action]]
        except (KeyError, AttributeError):
            return super(MultiPermissionViewSetMixin, self).get_permissions()
