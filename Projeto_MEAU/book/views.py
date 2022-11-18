from django.shortcuts import redirect, render
from .models import Voo, Historico
from .forms import criaVoo, criaHistorico
from django.shortcuts import redirect
from django.contrib import messages
import sqlite3
from datetime import datetime

# Create your views here.

# def handle500(request):
#     return render(request, "handle500.html")

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
        Voo.objects.create(codigoVoo=codigoVoo, companhia=companhia,
                       origem=origem, destino=destino, horarioProgramado=horarioProgramado)

    return render(request, "cadastrar.html")

def consultar(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaGeral']
        voos = voos.filter(codigoVoo__icontains=codigo)
            
    return render(request, "consultar.html", {'voos': voos})

def monitoring(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaVoos']
        voos = voos.filter(codigoVoo__icontains=codigo)
            
    return render(request, "monitoring.html", {'voos': voos,'historicos': historicos})

def reports(request):
    return render(request, "reports.html")

# def atrasos(request):
#     return render(request, "atrasos.html")

def dinamico(request):
    if request.method == 'POST':
        form = criaHistorico(request.POST)
        if form.is_valid():
            hist = form.save()
            return redirect('monitoramento')

    else:
        form = criaHistorico()
        
    return render(request,
                'dinamico.html',
                {'form': form})

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

def preenchimentoAtrasos(request):

    # historicos = Historico.objects.select_related("voo")
    # print(historicos.query)
    # print(historicos)

    atrasados = Historico.objects.raw("SELECT * FROM historico JOIN voo ON historico.voo_id = voo.id")
    print(atrasados.query)

    # print(atrasados.query)
    # print(atrasados)

    if request.method == 'POST':
        listaNames = ['origem', 'destino', 'dataInicio', 'dataFinal', 'codigoEmpresa', 'madrugada', 'manha', 'tarde', 'noite']
        listaRespostas = list()
        print('oiii')

        for i in range(len(listaNames)):
            try:
                listaRespostas.append(request.POST[listaNames[i]])
            except Exception as e:
                listaRespostas.append('off')

        print('oii2i')

        #filtra a origem se necessário
        if listaRespostas[0]!='':
            atrasados = atrasados.filter(origem=listaRespostas[0])

        print('oii3i')
        #filtra a destino se necessário
        if listaRespostas[1]!='':
            atrasados = atrasados.filter(destino=listaRespostas[1])

        print('oii4i')
        #aplicada datas
        
        dataMin = datetime.strptime(str(listaRespostas[2]),'%Y-%m-%d')
        print(dataMin)
        dataMax = datetime.strptime(str(listaRespostas[3]),'%Y-%m-%d')
        print(dataMax)
        atrasados = atrasados.filter(data__gst=dataMin)
        atrasados = atrasados.filter(data__lst=dataMax)


        #filtra a destino se necessário
        if listaRespostas[4]!='':
            atrasados = atrasados.filter(companhia=listaRespostas[4])        

    return render(request, "preenchimentoAtrasos.html")

def preenchimentoCancelamentos(request):
    return render(request, "preenchimentoCancelamentos.html")

