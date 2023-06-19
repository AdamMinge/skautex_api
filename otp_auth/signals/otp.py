# Django import
from django.dispatch import Signal


user_authenticated = Signal(providing_args=["user", 'request'])
user_verified = Signal(providing_args=["user", 'request'])
