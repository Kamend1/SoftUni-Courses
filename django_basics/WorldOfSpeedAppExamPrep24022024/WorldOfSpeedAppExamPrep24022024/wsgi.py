"""
WSGI config for WorldOfSpeedAppExamPrep24022024 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WorldOfSpeedAppExamPrep24022024.settings')

application = get_wsgi_application()
