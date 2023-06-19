# Python import
from os import environ
# Third-Part import
from split_settings.tools import optional, include


ENV = environ.get('DJANGO_ENV', 'development')

base_settings = [
    'components/common.py',
    'components/admin.py',
    'components/database.py',
    'components/docs.py',
    'components/email.py',
    'components/storage.py',
    'components/notification.py',
    'environments/{0}.py'.format(ENV),
    optional('environments/local.py'),
]

include(*base_settings)
