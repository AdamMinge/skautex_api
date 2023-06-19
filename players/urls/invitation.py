# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from players.views import InvitationViewSet

invitation_router = routers.SimpleRouter()
invitation_router.register('invitations', InvitationViewSet, basename='invitation')

urlpatterns = [
    path('', include(invitation_router.urls)),
]
