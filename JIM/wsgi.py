import os
import sys

from django.core.wsgi import get_wsgi_application


settings = 'JIM.settings.dev_settings' if sys.platform == 'darwin' else 'JIM.settings.prod_settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

application = get_wsgi_application()
