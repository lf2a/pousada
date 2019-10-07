# django
from django.urls import path

# local django
from .views import home, imagem

urlpatterns = [
    # /
    path('', home, name='home'),
    
    # /imagem/
    # administrar imagens enviadas
    path('imagem/', imagem, name='imagem'),
]
