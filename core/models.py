# django
from django.db import models
from django.utils.timezone import now

# local django
from cliente.models import User
from quarto.models import Quarto


class Reserva(models.Model):
    # um cliente pode ter várias reservas
    # ao excluir um cliente a reserva é excluída
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    # uma reserva pode possui apenas um quarto
    # ao excluir o quarto a reserva é excluída
    quarto = models.OneToOneField(Quarto, on_delete=models.CASCADE)

    total = models.DecimalField(max_digits=7, decimal_places=2)
    inicio = models.DateField(default=now)
    termino = models.DateField(default=now)

    def __str__(self):
        return '[ %s ] %s %s' % (self.cliente.username, self.quarto.numero, self.quarto.andar)
