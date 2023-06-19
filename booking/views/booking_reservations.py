# Django import
from django.utils.decorators import method_decorator
# Third-Party import
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from booking.serializers import BookingReservationsSerializer, BookingReservationsCreateUpdateSerializer
from booking.policies import BookingReservationsAccessPolicy
from booking.filters import BookingReservationsFilter
from booking.models import BookingReservations


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={status.HTTP_201_CREATED: BookingReservationsSerializer()}))
@method_decorator(name='update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingReservationsSerializer()}))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    responses={status.HTTP_200_OK: BookingReservationsSerializer()}))
class BookingReservationsViewSet(mixins.MultiSerializerViewSetMixin,
                                 mixins.CreateModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):

    permission_classes = (BookingReservationsAccessPolicy,)
    serializer_class = BookingReservationsSerializer
    response_serializer = BookingReservationsSerializer
    serializer_action_classes = {
        'create': BookingReservationsCreateUpdateSerializer,
        'update': BookingReservationsCreateUpdateSerializer,
        'partial_update': BookingReservationsCreateUpdateSerializer,
    }
    filter_class = BookingReservationsFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=BookingReservations)
    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, BookingReservations.objects.all()
        )
