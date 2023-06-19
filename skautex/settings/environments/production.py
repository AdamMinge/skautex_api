# Python import
import os
import ast
# Third-Part import
from corsheaders.defaults import default_headers


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', [])

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DOCS_ENABLE = False
HEALTH_CHECK_ENABLE = False

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', [])
CORS_ALLOWED_ORIGIN_REGEXES = os.environ.get('CORS_ALLOWED_ORIGIN_REGEXES', [])
CORS_ADDITIONAL_ALLOW_HEADERS = ast.literal_eval(os.environ.get('CORS_ADDITIONAL_ALLOW_HEADERS', '[]'))
CORS_ALLOW_HEADERS = os.environ.get('CORS_ALLOW_HEADERS', list(default_headers)) + CORS_ADDITIONAL_ALLOW_HEADERS

ADMIN_NAME = os.environ.get('ADMIN_NAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'uzumymwuzumymw')
ADMIN_MAIL = os.environ.get('ADMIN_MAIL', 'skautex@gmail.com')
