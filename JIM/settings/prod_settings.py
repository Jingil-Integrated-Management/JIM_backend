from JIM.settings.dev_settings import DEBUG, SECRET_KEY
from .base_settings import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True  # TODO False on actual production
ALLOWED_HOSTS = ['34.64.175.67']
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
