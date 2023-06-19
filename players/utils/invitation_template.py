import os


def create_invitation_template_path(instance, filename):
    return os.path.join(
        'players/invitations/templates',
        filename
    )