# Django import
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from core.decorators import swagger_fake_get_queryset
from contact_details.models import ContactDetail
from contact_details.filters import ContactDetailFilter
from accounts.serializers import UserContactDetailSerializer
from accounts.policies import UserContactDetailAccessPolicy


class UserContactDetailViewSet(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               viewsets.GenericViewSet):

    permission_classes = (UserContactDetailAccessPolicy,)
    serializer_class = UserContactDetailSerializer
    filter_class = ContactDetailFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    @swagger_fake_get_queryset(model=ContactDetail)
    def get_queryset(self):
        ct = ContentType.objects.get_for_model(get_user_model())
        return self.access_policy.scope_queryset(
            self.request, ContactDetail.objects.filter(content_type=ct, object_id=self.kwargs['user_id'])
        )
