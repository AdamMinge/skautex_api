# Python import
import os
import ast


DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['*'])

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DOCS_ENABLE = True
HEALTH_CHECK_ENABLE = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

VERIFICATION_DEBUG_USERS = ast.literal_eval(os.environ.get('VERIFICATION_DEBUG_USERS', '[]'))
VERIFICATION_DEBUG_CODE = os.environ.get('VERIFICATION_DEBUG_CODE', None)

ADMIN_NAME = os.environ.get('ADMIN_NAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'uzumymwuzumymw')
ADMIN_MAIL = os.environ.get('ADMIN_MAIL', 'skautex@gmail.com')
