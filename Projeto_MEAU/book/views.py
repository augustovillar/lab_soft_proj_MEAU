from django.shortcuts import redirect, render
from .models import Voo, Historico
from .forms import criaVoo, criaHistorico
from django.shortcuts import redirect
from django.contrib import messages
import sqlite3
from datetime import datetime

# Create your views here.

def handle500(request):
    return render(request, "handle500.html")

def login(request):
    return render(request, "login.html")

def crud(request):
    return render(request, "crud.html") 
 
def atualizar(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaAtualizar']
        voos = voos.filter(codigoVoo__icontains=codigo)
            
    return render(request, "atualizar.html", {'voos': voos})

def modificar(request, codigoVoo):
    voo = Voo.objects.get(codigoVoo__icontains = codigoVoo)
    return render(request, "modificar.html", {"voo": voo})

def posModificar(request, codigoVoo):
    if (request.method == 'POST'):
        voo = Voo.objects.get(codigoVoo__icontains = codigoVoo)
        voo.codigoVoo = request.POST.get("cadastroCodigoVoo")
        voo.companhia = request.POST.get("cadastroCompanhia")
        voo.origem = request.POST.get("cadastroOrigem")
        voo.destino = request.POST.get("cadastroDestino")
        voo.horarioProgramado = request.POST.get("cadastroHorarioProgramado")
        voo.save()

    return redirect("atualizar")


def createView(request):
    if (request.method == 'POST'):
        codigoVoo = request.POST.get("cadastroCodigoVoo")
        companhia = request.POST.get("cadastroCompanhia")
        origem = request.POST.get("cadastroOrigem")
        destino = request.POST.get("cadastroDestino")
        horarioProgramado = request.POST.get("cadastroHorarioProgramado")
        messages.success(request, 'O voo foi cadastrado com sucesso.')
        voo = Voo.objects.create(codigoVoo=codigoVoo, companhia=companhia,
                       origem=origem, destino=destino, horarioProgramado=horarioProgramado)
        if (voo.origem != "GRU"):
            Historico.objects.create(voo = voo, status = "EM_VOO")
        else:
            Historico.objects.create(voo = voo, status = "PREVISTO")

    return render(request, "cadastrar.html")

def consultar(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaGeral']
        voos = voos.filter(codigoVoo__icontains=codigo)
            
    return render(request, "consultar.html", {'voos': voos})
    
def painel(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    return render(request, "painel.html", {'voos': voos,'historicos': historicos})

def monitoring(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaVoos']
        voos = voos.filter(codigoVoo__icontains=codigo)
            
    return render(request, "monitoring.html", {'voos': voos, 'historicos': historicos})

def reports(request):
    return render(request, "reports.html")


def dinamico(request, id):
    formD = Historico.objects.get(voo_id = id)
    return render(request, "dinamico.html", {"formD": formD})

def posDinamico(request, id):
    if (request.method == 'POST'):
        voo = Historico.objects.get(id = id)
        voo.voo = Voo.objects.get(codigoVoo = request.POST.get("dinaVoo"))
        voo.data = request.POST.get("dinaData")
        voo.status = request.POST.get("dinaStatus")
        voo.horarioReal = request.POST.get("dinaHorario")
        voo.save()

    return redirect("monitoramento")

def erro_monitoramento(request):
    return render(request, "erro_monitoramento.html")

def cancelamento(request):
    return render(request, "cancelamento.html")

def relatorio(request):
    return render(request, "relatorio.html")

def remover(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaRemover']
        voos = voos.filter(codigoVoo=codigo)
            
    return render(request, "remover.html", {'voos': voos})

def confirmaRemover(request, codigoVoo):
    voo = Voo.objects.get(codigoVoo = codigoVoo)
    voo.delete()
    return redirect("remover")

def preenchimentoPeriodo(request):

    periodos = Historico.objects.select_related("voo")    

    if request.method == 'POST':
        dataInicio = request.POST["dataInicio"]
        dataFinal = request.POST["dataFinal"]
        codigoEmpresa = request.POST["codigoEmpresa"]
        horarioInicial = request.POST["horarioInicial"]
        horarioFinal = request.POST["horarioFinal"]

        if dataInicio != "":
            periodos = periodos.filter(data__gte=dataInicio)

        if dataFinal != "":
            periodos = periodos.filter(data__lte=dataFinal)

        if codigoEmpresa != "":
            periodos = periodos.filter(companhia=codigoEmpresa)

        if horarioInicial != "":
            periodos = periodos.filter(horarioReal__gte=horarioInicial)

        if horarioFinal != "":
            periodos = periodos.filter(horarioReal__lte=horarioFinal)

        

    return render(request, "preenchimentoPeriodo.html", {'periodos': periodos})
    
def preenchimentoCancelamentos(request):
    historicos = Historico.objects.select_related("voo")
    cancelados = historicos.filter(status = "CANCELADO")
    
    if request.method == 'POST':
        dataIncio = request.POST['dataInicio']
        if dataIncio != "":
            cancelados = cancelados.filter(data__gte=dataIncio)

        dataFinal = request.POST['dataFinal']
        if dataFinal != "":
            cancelados = cancelados.filter(data__lte=dataFinal)


    return render(request, "preenchimentoCancelamentos.html", {'cancelados': cancelados})

