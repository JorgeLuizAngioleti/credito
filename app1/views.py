from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Entrada
from .forms import EntradaForm,  NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
def home(request):
    context={}
    tudo_ent = Entrada.objects.all()
    for i in tudo_ent:
        print(i.valor,i.parcela)
    context['todas_e']=tudo_ent
    return render(request,'app1/home.html', context)

def boasvindas(request):
    context = {}
    return render(request, 'app1/boasvindas.html', context)


def capa(request):
    context = {}
    return render(request, 'app1/index.html', context)

def logout1(request):
    logout(request)
    return redirect('url_boasvindas')

@login_required
def AddEntrada(request):
    nome = request.user.first_name
    context={}
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_home')
    else:
        form = EntradaForm(initial={"nome":nome})
    context['form']=form
    context['identificacao'] = "Entrada"
    return render(request,'app1/form.html',context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			s = form.save()
			s.set_password(s.password)
			s = form.save()
			messages.success(request, "Registrado com sucesso!" )
			return redirect("login")
		messages.error(request, "Usuario não registrado, informações invalidas.")
	form = NewUserForm
	return render (request=request, template_name="app1/cadastro.html", context={"form":form})

