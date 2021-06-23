from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Entrada, Valor, Parcelas
from .forms import EntradaForm,  NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
def home(request):
    nome = request.user.first_name
    context={}
    tudo_ent = Entrada.objects.filter(nome=nome)
    context['todas_e']=tudo_ent
    return render(request,'app1/home.html', context)

def boasvindas(request):
    context = {}
    return render(request, 'app1/boasvindas.html', context)

def comprar(request, id):
    obj = Entrada.objects.get(pk=id)
    obj.fechou_negocio = True
    obj.save()
    messages.success(request, "Solicitação de emprestimo realizada com sucesso!!")
    return redirect('url_home')

def escolher(request):
    nome = request.user.first_name
    context = {}
    valor = Valor.objects.all()
    parcela = Parcelas.objects.all()
    if request.method == 'POST':
        val = request.POST.get('valor')
        par = request.POST.get('parcelas')
        print(val,par)
        request.session['val'] = val
        request.session['par'] = par
        return redirect("url_entrada")
    else:
        context['valores'] = valor
        context['parcelas'] = parcela
        return render(request, 'app1/escolha.html', context)


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
        val = request.session['val']
        par = request.session['par']
        print("add",val)
        form = EntradaForm(initial={"nome":nome,"valor":val,"parcela":par})
    context['form']=form
    context['identificacao'] = "Confira seus dados para finalizar"
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

