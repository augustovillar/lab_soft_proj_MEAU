from django.contrib import admin
from django.urls import path
from book import views

handler500 = 'book.views.handle500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('crud/', views.crud, name = "crud"),
    path('atualizar/', views.atualizar, name = "atualizar"),

    path('modificar/', views.modificar, name = "modificar"),
    path('cadastrar/', views.createView, name = "create"),
    path('consultar/', views.consultar, name = "consultar"),
    path('partidas/', views.partidas, name="partidas"),
    path('chegadas/', views.chegadas, name="chegadas"),

    path('dinamico/', views.dinamico),
    
    path('relatorio/', views.relatorio),
    path('remover/', views.remover),
   
   
    path('monitoring/', views.monitoring),
    path('preenchimentoAtrasos/', views.preenchimentoAtrasos),
    path('preenchimentoCancelamentos/', views.preenchimentoCancelamentos),
    path('reports/', views.reports),
]
