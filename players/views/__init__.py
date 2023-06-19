from players.views.player import PlayerViewSet
from players.views.team import TeamViewSet
from players.views.league import LeagueViewSet
from players.views.player_contact_detail import PlayerContactDetailViewSet
from players.views.invitation import InvitationViewSet
from players.views.invitation_template import InvitationTemplateViewSet

__all__ = ['PlayerViewSet', 'TeamViewSet', 'LeagueViewSet',
           'PlayerContactDetailViewSet', 'InvitationViewSet',
           'InvitationTemplateViewSet']
