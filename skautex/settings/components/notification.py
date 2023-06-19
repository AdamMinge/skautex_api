import os

FCM_DJANGO_SETTINGS = {
        "APP_VERBOSE_NAME": "Skautex",
        "FCM_SERVER_KEY": os.environ.get('FCM_SERVER_KEY', ''),
        "ONE_DEVICE_PER_USER": True,
        "DELETE_INACTIVE_DEVICES": True,
}
