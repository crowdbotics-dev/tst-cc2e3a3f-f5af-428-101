"""
WSGI config for tst_cc2e3a3f_f5af_428_101 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_cc2e3a3f_f5af_428_101.settings"
)

application = get_wsgi_application()
