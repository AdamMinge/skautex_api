# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from booking.serializers import BookingBlacklistSerializer, BookingBlacklistCreateUpdateSerializer
from booking.policies import BookingBlacklistAccessPolicy
from booking.filters import BookingBlacklistFilter
from booking.models import BookingBlacklist


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: BookingBlacklistSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingBlacklistSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingBlacklistSerializer()}))
class BookingBlacklistViewSet(mixins.MultiSerializerViewSetMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):

    permission_classes = (BookingBlacklistAccessPolicy,)
    serializer_class = BookingBlacklistSerializer
    response_serializer = BookingBlacklistSerializer
    serializer_action_classes = {
        'create': BookingBlacklistCreateUpdateSerializer,
        'update': BookingBlacklistCreateUpdateSerializer,
        'partial_update': BookingBlacklistCreateUpdateSerializer,
    }
    filter_class = BookingBlacklistFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, BookingBlacklist.objects.all()
        )
