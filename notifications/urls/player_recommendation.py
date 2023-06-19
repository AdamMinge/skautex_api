# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from notifications.views import PlayerRecommendationViewSet

player_recommendation_router = routers.SimpleRouter()
player_recommendation_router.register('player_recommendations', PlayerRecommendationViewSet, basename='player_recommendation')

urlpatterns = [
    path('', include(player_recommendation_router.urls)),
]
