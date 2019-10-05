# django
from django.urls import path

# local django
from .views import reservar_quarto, excluir_reserva

urlpatterns = [
    # /reserva/<str:id_quarto>/
    path('<str:id_quarto>', reservar_quarto, name='reserva'),

    # /reserva/<str:id_quarto>/excluir
    path('<str:id_quarto>/excluir/', excluir_reserva, name='excluir')
]
