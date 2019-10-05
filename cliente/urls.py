# django
from django.urls import path

# local django
from .views import buscar_minhas_reservas, atualizar_informacoes, excluir

urlpatterns = [
    path('', buscar_minhas_reservas, name='reservas'),
    path('usuario/atualizar/', atualizar_informacoes, name='atualizar'),
    path('usuario/excluir/', excluir, name='excluir_conta'),
]
