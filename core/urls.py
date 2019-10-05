# django
from django.urls import path

# local django
from .views import reservar_quarto, excluir_reserva

urlpatterns = [
    path('<str:id_quarto>', reservar_quarto, name='reserva'),
    path('<str:id_quarto>/excluir/', excluir_reserva, name='excluir')
]
