# python standard library
import os

# django
from django.core.wsgi import get_wsgi_application

# external library
from dj_static import Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pousada.settings')

application = Cling(get_wsgi_application())
