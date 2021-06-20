from django.contrib import admin
from .models import Entrada, Saida, User
# Register your models here.
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(User)
