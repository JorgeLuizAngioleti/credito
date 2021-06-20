from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField

# Create your models here.
class Entrada(models.Model):
    nome = models.CharField(u'Gastos de entrada',max_length=150)
    data = models.DateTimeField( default=timezone.now)
    entrada = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class Saida(models.Model):
    nome = models.CharField(u'Gastos de saída',max_length=150)
    data = models.DateTimeField( default=timezone.now)
    saida = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nome
class Cliente(models.Model):
    nome = models.CharField(u'Nome completo', max_length=50)
    idade = models.IntegerField(u'Idade',max_length=3)
    cpf = CPFField('cpf')
    def __str__(self):
        return self.nome
