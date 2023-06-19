# Third-Party import
from rest_framework.response import Response
from rest_framework import status, viewsets
# Local import
from notifications.serializers import PlayerRecommendationSerializer
from notifications.policies import PlayerRecommendationAccessPolicy


class PlayerRecommendationViewSet(viewsets.GenericViewSet):
    permission_classes = (PlayerRecommendationAccessPolicy,)
    serializer_class = PlayerRecommendationSerializer

    def create(self, request, *args, **kwargs):
        serializer = PlayerRecommendationSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.send_notification()
        return Response(status=status.HTTP_201_CREATED)
