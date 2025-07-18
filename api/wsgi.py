import os

from django.core.wsgi import get_wsgi_application
setting_module ='api.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'api.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_module)



application = get_wsgi_application()
