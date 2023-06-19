# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from players.views import TeamViewSet

router = routers.SimpleRouter()
router.register('teams', TeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls)),
]
