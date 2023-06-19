# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from accounts.views import UserViewSet

user_router = routers.SimpleRouter()
user_router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(user_router.urls)),
]
