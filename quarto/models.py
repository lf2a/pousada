from django.db import models


class Quarto(models.Model):
    numero = models.CharField(max_length=10)
    andar = models.IntegerField()
    banheiro = models.IntegerField()
    cama = models.IntegerField()
    diaria = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '[ %s ] %s' % (self.andar, self.numero)


class ImagemQuarto(models.Model):
    url = models.ImageField(upload_to='quarto_imagens')
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return '[ %s ] %s' % (self.quarto.andar, self.quarto.numero)