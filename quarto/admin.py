from django.contrib import admin

# django local
from .models import Quarto, ImagemQuarto

admin.site.register(Quarto)
admin.site.register(ImagemQuarto)