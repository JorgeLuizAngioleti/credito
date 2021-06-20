from django.contrib import admin
from .models import Entrada, User, Banco, Valor, Parcelas
# Register your models here.
admin.site.register(Entrada)
admin.site.register(User)
admin.site.register(Banco)
admin.site.register(Valor)
admin.site.register(Parcelas)
