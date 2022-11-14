from django.shortcuts import redirect, render
from .models import Voo, Historico
from .forms import buscaVoo, atualizaVoo, criaVoo

# Create your views here.

def crud(request):

    return render(request, "crud.html")

def login(request):
    return render(request, "login.html")

def modificar(request):
    return render(request, "modificar.html")

def monitoring(request):
    return render(request, "monitoring.html")

def reports(request):
    return render(request, "reports.html")

def atrasos(request):
    return render(request, "atrasos.html")

def atualizar(request):
    if request.method == "POST":
        form = atualizaVoo(request.POST)
        if form.is_valid():
            form.update()
    else:
        form = atualizaVoo()
    return render(request, "atualizar.html", {'form': form})    

def cadastrar(request):
    if request.method == "POST":
        form = criaVoo(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = criaVoo()
    return render(request, "cadastrar.html", {'form': form})

def cancelamento(request):
    return render(request, "cancelamento.html")

def consultar(request):
    if request.method == "POST":
        form = buscaVoo(request.POST)
        if form.is_valid():
            return redirect("visualizavoo")
    else:
        form = buscaVoo()
    return render(request, "consultar.html", {'form': form})

def dinamico(request):
    return render(request, "dinamico.html")

def modificar(request):
    return render(request, "modificar.html")

def relatorio(request):
    return render(request, "relatorio.html")

def remover(request):
    return render(request, "remover.html")

def preenchimentoAtrasos(request):
    return render(request, "preenchimentoAtrasos.html")

def preenchimentoCancelamentos(request):
    return render(request, "preenchimentoCancelamentos.html")

def visualizavoo(request):
    return render(request, "visualizavoo.html")
