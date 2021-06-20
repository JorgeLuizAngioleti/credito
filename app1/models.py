from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class Banco(models.Model):
    nome = models.CharField(u'Informe seu banco',max_length=80,)
    def __str__(self):
        return self.nome

class Valor(models.Model):
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self):
        return str(self.valor)

class Parcelas(models.Model):
    parcelas = models.IntegerField(default=6)
    def __str__(self):
        return str(self.parcelas)

class Entrada(models.Model):
    nome = models.CharField(u'Usuario',max_length=150)
    data = models.DateTimeField( default=timezone.now)
    valor = models.ForeignKey(Valor, on_delete=models.CASCADE)
    parcela = models.ForeignKey(Parcelas, on_delete=models.CASCADE)
    fechou_negocio = models.BooleanField(u'comprou',default=False)


    def __str__(self):
        return self.nome

class User(AbstractUser):
    nome = models.CharField(u'Endereço', max_length=50)
    idade = models.IntegerField(default=0)
    telefone = models.CharField(u'Telefone', max_length=50)
    cpf = CPFField('cpf')
   # banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    #esc = models.ForeignKey(Escola, on_delete=models.CASCADE)
    #per1 = models.BooleanField(u'Permição 1',default=False)

