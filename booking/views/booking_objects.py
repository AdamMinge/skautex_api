# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from booking.serializers import BookingObjectsSerializer, BookingObjectsCreateUpdateSerializer
from booking.policies import BookingObjectsAccessPolicy
from booking.filters import BookingObjectsFilter
from booking.models import BookingObjects


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: BookingObjectsSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingObjectsSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingObjectsSerializer()}))
class BookingObjectsViewSet(mixins.MultiSerializerViewSetMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    permission_classes = (BookingObjectsAccessPolicy,)
    serializer_class = BookingObjectsSerializer
    response_serializer = BookingObjectsSerializer
    serializer_action_classes = {
        'create': BookingObjectsCreateUpdateSerializer,
        'update': BookingObjectsCreateUpdateSerializer,
        'partial_update': BookingObjectsCreateUpdateSerializer,
    }
    filter_class = BookingObjectsFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, BookingObjects.objects.all()
        )
