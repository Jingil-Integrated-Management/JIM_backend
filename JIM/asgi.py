"""
ASGI config for JIM project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

settings = 'JIM.settings.dev_settings' if sys.platform == 'darwin' else 'JIM.settings.prod_settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

application = get_asgi_application()
