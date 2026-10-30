
from django.db import models


class Corte(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao = models.PositiveIntegerField(
        help_text="Duração do serviço em minutos"
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'

    def __str__(self):
        return self.nome