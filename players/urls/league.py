# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from players.views import LeagueViewSet

router = routers.SimpleRouter()
router.register('leagues', LeagueViewSet, basename='league')

urlpatterns = [
    path('', include(router.urls)),
]
