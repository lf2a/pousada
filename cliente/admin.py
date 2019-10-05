# django
from django.contrib import admin

# local django
from .models import User

# registrando o model
admin.site.register(User)