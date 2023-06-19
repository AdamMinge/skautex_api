# Python import
import os
# Local import
from skautex.settings.components.common import BASE_DIR


try:
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': os.environ['SQL_DB_NAME'],
            'USER': os.environ['SQL_USERNAME'],
            'PASSWORD': os.environ['SQL_PASSWORD'],
            'HOST': os.environ['SQL_HOSTNAME'],
            'PORT': os.environ['SQL_PORT'],
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
except KeyError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
