# Django import
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
# Third-Party import
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.compat import coreapi, coreschema


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    limit_query_description = _('Number of results to return per page or none to return all results after offset.')

    def __check_if_limit_is_none(self, request):
        if self.limit_query_param in request.query_params:
            return request.query_params[self.limit_query_param] == 'none'
        return False

    def get_limit(self, request):
        if self.__check_if_limit_is_none(request):
            return self.count - self.get_offset(request)
        else:
            return super().get_limit(request)

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.limit_query_param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title='Limit',
                    description=force_str(self.limit_query_description)
                )
            ),
            coreapi.Field(
                name=self.offset_query_param,
                required=False,
                location='query',
                schema=coreschema.Integer(
                    title='Offset',
                    description=force_str(self.offset_query_description)
                )
            )
        ]