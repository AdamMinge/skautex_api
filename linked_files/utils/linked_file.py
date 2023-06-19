import os


def create_lined_file_path(instance, filename):
    return os.path.join(
        'reports',
        filename
    )
