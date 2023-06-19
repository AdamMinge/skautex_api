# Third-Party import
from rest_framework import viewsets
# Local import
from core import mixins
from players.models import League
from players.serializers import LeagueSerializer
from players.policies import LeagueAccessPolicy
from players.filters import LeagueFilter


class LeagueViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = (LeagueAccessPolicy,)
    serializer_class = LeagueSerializer
    filter_class = LeagueFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, League.objects.all()
        )
