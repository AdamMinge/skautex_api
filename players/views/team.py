# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from players.models import Team
from players.serializers import TeamSerializer
from players.policies import TeamAccessPolicy
from players.filters import TeamFilter


class TeamViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (TeamAccessPolicy,)
    serializer_class = TeamSerializer
    filter_class = TeamFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Team.objects.all()
        )
