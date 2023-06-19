# Python import
from itertools import chain
# Third-Party import
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
# Local import
from core import mixins
from players.models import PlayerPositionChoice
from rankings.models import Ranking
from rankings.serializers import RankingSerializer
from rankings.policies import RankingAccessPolicy
from rankings.filters import RankingFilter


class RankingViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (RankingAccessPolicy,)
    serializer_class = RankingSerializer
    filter_class = RankingFilter
    lookup_field = 'id'

    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, Ranking.objects.all()
        )

    def __get_top5_queryset(self):
        queryset = self.get_queryset()
        position_top5_id_list = []
        for position_choice in PlayerPositionChoice.choices:
            position_top5_id_list.append(queryset
                                         .filter(player__position=position_choice[0])
                                         .order_by('-score')
                                         .values_list('id', flat=True)[:5])
        position_top5_id_list = list(chain(*position_top5_id_list))
        return queryset.order_by('-score').filter(id__in=position_top5_id_list)

    @action(detail=False, methods=['get'], url_path='top5')
    def get_top5_ranking(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.__get_top5_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
