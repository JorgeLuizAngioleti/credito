from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
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

class User(AbstractUser):
    nome = models.CharField(u'Nome completo', max_length=50)
    idade = models.IntegerField()
    cpf = CPFField('cpf')
    birth_date = models.DateField(null=True, blank=True)
    #esc = models.ForeignKey(Escola, on_delete=models.CASCADE)
    #per1 = models.BooleanField(u'Permição 1',default=False)

