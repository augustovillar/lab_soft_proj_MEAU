import re
from django.shortcuts import render

# Create your views here.

def crud(request):
    return render(request, "crud.html")

def homepage(request):
    return render(request, "homepage.html")

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
    return render(request, "atualizar.html")

def cadastrar(request):
    return render(request, "cadastrar.html")

def cancelamento(request):
    return render(request, "cancelamento.html")

def consultar(request):
    return render(request, "consultar.html")

def dinamico(request):
    return render(request, "dinamico.html")

def modificar(request):
    return render(request, "modificar.html")

def relatorio(request):
    return render(request, "relatorio.html")

def remover(request):
    return render(request, "remover.html")

def preenchimento(request):
    return render(request, "preenchimento.html")

def visualizavoo(request):
    return render(request, "visualizavoo.html")
