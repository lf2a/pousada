# django
from django.contrib import admin

# local django
from .models import Reserva

# registra o model
admin.site.register(Reserva)