"""
WSGI config for geodjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

sys.path.append("/opt/venv/lib/python2.7/site-packages")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".settings")

application = get_wsgi_application()
