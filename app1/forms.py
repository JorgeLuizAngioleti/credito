from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Entrada, Saida, User
from django.forms import ModelForm
class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','cpf','idade', 'nome']

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(UserForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user

class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entrada
        fields = ('nome', 'entrada',)

class SaidaForm(forms.ModelForm):

    class Meta:
        model = Saida
        fields = ('nome', 'saida',)