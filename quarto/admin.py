# django
from django.contrib import admin

# django local
from .models import Quarto, ImagemQuarto

# registrando models
admin.site.register(Quarto)
admin.site.register(ImagemQuarto)