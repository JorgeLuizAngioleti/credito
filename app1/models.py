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
    valor = models.CharField(u'Valor',max_length=10)
    def __str__(self):
        return str(self.valor)

class Parcelas(models.Model):
    parcelas = models.IntegerField(default=6)
    def __str__(self):
        return str(self.parcelas)

class Entrada(models.Model):

    nome = models.CharField(u'Usuario',max_length=150)
    data = models.DateTimeField( default=timezone.now)
    valor = models.CharField(u'Valor',max_length=10)
    parcela = models.IntegerField(default=6)
    fechou_negocio = models.BooleanField(u'Comprar o plano',default=False)
    aprovado = models.BooleanField(u'comprou',default=False)

    def __str__(self):
        return self.nome

    def calcular(self):
        return "{:.2f}".format((float(self.valor)/float(self.parcela)))


    def juros(self):
        return float(self.valor)*0.04+float(self.valor)


class User(AbstractUser):
    nome = models.CharField(u'Endereço', max_length=50)
    idade = models.IntegerField(default=0)
    telefone = models.CharField(u'Telefone', max_length=50)
    cpf = CPFField('cpf')
   # banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

