from django.shortcuts import redirect, render
from .models import Voo, Historico
from .forms import criaVoo
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def handle500(request):
    return render(request, "handle500.html")

def login(request):
    return render(request, "login.html")

def crud(request):
    return render(request, "crud.html")

# def atualizarOriginal(request):
#     if request.method == "POST":
#         form = atualizaVoo(request.POST)
#         if form.is_valid():
#             form.update()
#     else:
#         form = atualizaVoo()
#     return render(request, "atualizar.html", {'form': form})    

def atualizar(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaAtualizacao']
        voos = voos.filter(codigoVoo=codigo)
            
    return render(request, "atualizar.html", {'voos': voos})

def modificar(request):
    
    if request.method =='POST':
        codigo = request.POST['atualiza']
        voo = Voo.objects.get(id=id)
        form = criaVoo(request.POST, instance=voo)
        if form.is_valid():
            form.save()
            return redirect('atualizar')
    else:
        form = criaVoo(instance=voo)
    
    form = criaVoo()

    return render(request,
                'modificar.html',
                {'form': form})



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


def partidas(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaPartidas']
        voos = voos.filter(codigoVoo=codigo)
            
    return render(request, "partidas.html", {'voos': voos})


def chegadas(request):
    historicos = Historico.objects.all()
    voos = Voo.objects.all()
    
    if request.method == 'POST':
        codigo = request.POST['buscaChegadas']
        voos = voos.filter(codigoVoo=codigo)
            
    return render(request, "chegadas.html", {'voos': voos})

def monitoring(request):
    return render(request, "monitoring.html")

def reports(request):
    return render(request, "reports.html")

def atrasos(request):
    return render(request, "atrasos.html")

def dinamico(request):
    return render(request, "dinamico.html")

def modificar(request):
    return render(request, "modificar.html")

def cancelamento(request):
    return render(request, "cancelamento.html")

def relatorio(request):
    return render(request, "relatorio.html")

def remover(request):
    return render(request, "remover.html")

def preenchimentoAtrasos(request):
    return render(request, "preenchimentoAtrasos.html")

def preenchimentoCancelamentos(request):
    return render(request, "preenchimentoCancelamentos.html")

