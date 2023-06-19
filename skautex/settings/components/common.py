# Python import
import os
import datetime


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CORS_ORIGIN_ALLOW_ALL = os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'True') == 'True'

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_api_key',
    'rest_framework_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_access_policy',
    'rest_framework_nested',
    'django_extensions',
    'djchoices',
    'djmoney',
    'colorfield',
    'storages',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_email',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
    'drf_yasg',
    'fcm_django',
    'core.apps.CoreConfig',
    'contact_details.apps.ContactDetailsConfig',
    'linked_files.apps.LinkedFilesConfig',
    'otp_auth.apps.OTPAuthConfig',
    'accounts.apps.AccountsConfig',
    'players.apps.PlayersConfig',
    'reports.apps.ReportsConfig',
    'rankings.apps.RankingsConfig',
    'cost_recording.apps.CostRecordingConfig',
    'booking.apps.BookingConfig',
    'calendars.apps.CalendarsConfig',
    'notifications.apps.NotificationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "otp_auth.permissions.HasOrganizationAPIKey",
        "otp_auth.permissions.Verified",
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework_filters.backends.RestFrameworkFilterBackend',
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.OptionalLimitOffsetPagination',
    'PAGE_SIZE': 10
}

SIMPLE_JWT = {
    'TOKEN_LIFETIME': datetime.timedelta(days=1),
    'TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=7),
}

API_KEY_CUSTOM_HEADER = "HTTP_API_KEY"

ROOT_URLCONF = 'skautex.urls'

AUTH_USER_MODEL = 'accounts.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skautex.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


