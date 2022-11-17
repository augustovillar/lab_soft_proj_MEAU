from django.contrib import admin
from django.urls import path
from book import views

# handler500 = 'book.views.handle500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('crud/', views.crud, name = "crud"),
    path('atualizar/', views.atualizar, name = "atualizar"),

    path('modificar/<str:codigoVoo>', views.modificar, name = "modificar"),
    path('posModificar/<str:codigoVoo>', views.posModificar, name = "posModificar"),
    path('cadastrar/', views.createView, name = "create"),
    path('consultar/', views.consultar, name = "consultar"),

    path('dinamico/', views.dinamico, name="dinamico"),
    
    path('relatorio/', views.relatorio),
    path('remover/', views.remover, name = "remover"),
    path('confirmaRemover/<str:codigoVoo>', views.confirmaRemover, name = "confirmaRemover"),
   
    path('monitoring/', views.monitoring, name = "monitoramento"),
    path('preenchimentoAtrasos/', views.preenchimentoAtrasos),
    path('preenchimentoCancelamentos/', views.preenchimentoCancelamentos),
    path('reports/', views.reports),
]
