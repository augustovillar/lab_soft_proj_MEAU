from django.shortcuts import redirect, render
from .models import Voo, Historico
from .forms import criaVoo, criaHistorico
from django.shortcuts import redirect
from django.contrib import messages

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
        voos = voos.filter(codigoVoo=codigo)
            
    return render(request, "atualizar.html", {'voos': voos})

def modificar(request, codigoVoo):
    voo = Voo.objects.get(codigoVoo = codigoVoo)
    return render(request, "modificar.html", {"voo": voo})

def posModificar(request, codigoVoo):
    if (request.method == 'POST'):
        voo = Voo.objects.get(codigoVoo = codigoVoo)
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
        voos = voos.filter(codigoVoo=codigo)
            
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
    historicos = Historico.objects.all()
    print("OLA TESTE")
    print(request)
    if request.method == 'POST':
        listaNames = ['origem', 'destino', 'dataInicio', 'dataFinal', 'codigoEmpresa', 'codigoAeroporto', 'madrugada', 'manha', 'tarde', 'noite']
        listaRespostas = list()

        for i in range(len(listaNames)):
            try:
                listaRespostas.append(request.POST[listaNames[i]])
            except Exception as e:
                listaRespostas.append('off')
        print(listaRespostas)

        # destino = request.POST['destino']
        # dataInicio = request.POST['dataInicio']
        # dataFinal = request.POST['dataFinal']
        # codigoEmpresa = request.POST['codigoEmpresa']
        # codigoAeroporto = request.POST['codigoAeroporto']

        # madrugada = request.POST['madrugada']
        # manha = request.POST['manha']
        # tarde = request.POST['tarde']
        # noite = request.POST['noite']

        # print(origem+" "+destino+" "+dataInicio+" "+dataFinal+" "+codigoEmpresa+" "+codigoAeroporto+" "+madrugada+" "+manha+" "+tarde+" "+noite)


    return render(request, "preenchimentoAtrasos.html")

# def monitoring(request):
#     historicos = Historico.objects.all()
#     voos = Voo.objects.all()
    
#     if request.method == 'POST':
#         codigo = request.POST['buscaVoos']
#         voos = voos.filter(codigoVoo__icontains=codigo)
            
#     return render(request, "monitoring.html", {'voos': voos,'historicos': historicos})

def preenchimentoCancelamentos(request):
    return render(request, "preenchimentoCancelamentos.html")

