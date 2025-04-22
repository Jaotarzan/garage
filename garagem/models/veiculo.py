from django.db import models

from garagem.models import Acessorio, Cor, Modelo

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio, blank=True)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acessorios = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"{self.id} {self.modelo} {self.cor} {self.ano}"
    