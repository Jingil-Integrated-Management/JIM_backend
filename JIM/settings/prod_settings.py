from JIM.settings.dev_settings import DEBUG, SECRET_KEY
from .base_settings import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True  # TODO False on actual production
ALLOWED_HOSTS = ['34.64.103.154', 'jim-backend.duckdns.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jim-backend',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '34.64.207.136',
        'PORT': '5432',
    }
}
