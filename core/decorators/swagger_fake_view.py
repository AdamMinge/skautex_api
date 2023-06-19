def swagger_fake_get_queryset(model):
    def wrap(method):
        def _impl(self, *method_args, **method_kwargs):
            if getattr(self, 'swagger_fake_view', False):
                return model.objects.none()
            else:
                return method(self, *method_args, **method_kwargs)
        return _impl
    return wrap
