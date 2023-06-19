# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from rankings.views import RankingViewSet

router = routers.SimpleRouter()
router.register('rankings', RankingViewSet, basename='ranking')

urlpatterns = [
    path('', include(router.urls)),
]
