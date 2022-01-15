from JIM.settings.dev_settings import DEBUG, SECRET_KEY
from .base_settings import *
import os

SECRET_KEY = os.environ.get('JIM_SECRET_KEY')
DEBUG = True  # TODO False on actual production
ALLOWED_HOSTS = ['34.64.181.1', 'jingilinc.duckdns.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jim_db',
        'USER': 'therealjamesjung',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = False
