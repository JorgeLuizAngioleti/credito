from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Entrada, Saida, Cliente
from .forms import EntradaForm, SaidaForm, NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
def home(request):
    context={}
    tudo_ent = Entrada.objects.all()
    tudo_sai = Saida.objects.all()
    ent = Entrada.objects.all().aggregate(e=Sum('entrada'))
    sai = Saida.objects.all().aggregate(s=Sum('saida'))
    context['entrada']=ent['e']
    context['saida']= sai['s']
    try:
        context['total']=ent['e']-sai['s']
    except:
        pass
    context['todas_e']=tudo_ent
    context['todas_s']=tudo_sai
    return render(request,'app1/home.html', context)

def boasvindas(request):
    context = {}
    return render(request, 'app1/boasvindas.html', context)


def capa(request):
    context = {}
    return render(request, 'app1/index.html', context)

@login_required
def AddEntrada(request):
    context={}
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_home')
    else:
        form = EntradaForm()
    context['form']=form
    context['identificacao'] = "Entrada"
    return render(request,'app1/form.html',context)
@login_required
def AddSaida(request):
    context={}
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_home')
    else:
        form = SaidaForm()
    context['form']=form
    context['identificacao']="Saída"
    return render(request,'app1/form.html',context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Registrado com sucesso!" )
			return redirect("login")
		messages.error(request, "Usuario não registrado, informações invalidas.")
	form = NewUserForm
	return render (request=request, template_name="app1/cadastro.html", context={"form":form})

