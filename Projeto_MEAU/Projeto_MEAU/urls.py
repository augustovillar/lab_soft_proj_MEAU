from django.contrib import admin
from django.urls import path, include
from book import views

handler500 = 'book.views.handle500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('crud/', views.crud, name = "crud"),
    path('atualizar/', views.atualizar, name = "atualizar"),
    path('__debug__/', include('debug_toolbar.urls')),
    path('modificar/<str:codigoVoo>', views.modificar, name = "modificar"),
    path('posModificar/<str:codigoVoo>', views.posModificar, name = "posModificar"),
    path('cadastrar/', views.createView, name = "create"),
    path('consultar/', views.consultar, name = "consultar"),

    path('dinamico/<int:id>', views.dinamico, name="dinamico"),
    path('posDinamico/<int:id>', views.posDinamico, name = "posDinamico"),
    path('relatorio/', views.relatorio),
    path('remover/', views.remover, name = "remover"),
    path('confirmaRemover/<str:codigoVoo>', views.confirmaRemover, name = "confirmaRemover"),
    path('erro_monitoramento/', views.erro_monitoramento, name = "erro_monitoramento"),
    path('monitoring/', views.monitoring, name = "monitoramento"),
    path('preenchimentoPeriodo/', views.preenchimentoPeriodo, name='periodo'),
    path('preenchimentoCancelamentos/', views.preenchimentoCancelamentos, name='cancelamento'),
    path('reports/', views.reports),
    path('painel/', views.painel),
]
