# Python import
import urllib.parse
# Django import
from django.urls import resolve
# Local import
from core.utils import model_field_exists


def __filter_kwargs(kwargs, model_cls):
    new_kwargs = {key: value for (key, value) in kwargs.items() if model_field_exists(model_cls, key)}
    return new_kwargs


def get_object_for_url(url):
    path = urllib.parse.urlparse(url).path
    resolved_func, unused_args, resolved_kwargs = resolve(path)
    resolved_model = resolved_func.cls.serializer_class.Meta.model
    resolved_kwargs = __filter_kwargs(resolved_kwargs, resolved_model)
    return resolved_func.cls.serializer_class.Meta.model.objects.get(**resolved_kwargs)
