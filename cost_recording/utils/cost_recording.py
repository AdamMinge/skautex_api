import os


def create_cost_recording_file_path(instance, filename):
    return os.path.join(
        'cost_recording',
        filename
    )
