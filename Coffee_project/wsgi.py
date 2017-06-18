import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# WSGI config for Coffee project

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Coffee-project.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
