# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from accounts.views import PermissionViewSet

router = routers.SimpleRouter()
router.register('permissions', PermissionViewSet, basename='permission')

urlpatterns = [
    path('', include(router.urls)),
]
