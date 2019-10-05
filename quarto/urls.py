# django
from django.urls import path

# local django
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
