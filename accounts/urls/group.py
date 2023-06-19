# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from accounts.views import GroupViewSet

router = routers.SimpleRouter()
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
