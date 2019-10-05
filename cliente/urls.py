# django
from django.urls import path

# local django
from .views import buscar_minhas_reservas, atualizar_informacoes, excluir

urlpatterns = [
    # /reservas/
    path('', buscar_minhas_reservas, name='reservas'),

    # /reservas/usuario/atualizar/
    path('usuario/atualizar/', atualizar_informacoes, name='atualizar'),

    # /reservas/usuario/excluir/
    path('usuario/excluir/', excluir, name='excluir_conta'),
]
