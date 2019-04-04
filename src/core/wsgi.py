"""
WSGI config for skeleton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

MODE = os.getenv('MODE')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{MODE}')

application = get_wsgi_application()
