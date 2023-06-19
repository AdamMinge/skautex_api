import os


def create_player_profile_picture_path(instance, filename):
    return os.path.join(
        'players',
        filename
    )
