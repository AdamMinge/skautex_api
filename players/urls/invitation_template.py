# Django import
from django.urls import include, path
# Third-Party import
from rest_framework import routers
# Local import
from players.views import InvitationTemplateViewSet

invitation_router = routers.SimpleRouter()
invitation_router.register('invitations_templates', InvitationTemplateViewSet, basename='invitation_template')

urlpatterns = [
    path('', include(invitation_router.urls)),
]
