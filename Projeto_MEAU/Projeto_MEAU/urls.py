"""Projeto_MEAU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atrasos/', views.atrasos),
    path('atualizar/', views.atualizar),
    path('cadastrar/', views.cadastrar),
    path('cancelamento/', views.cancelamento),
    path('consultar/', views.consultar),
    path('crud/', views.crud),
    path('dinamico/', views.dinamico),
    path('modificar/', views.modificar),
    path('relatorio/', views.relatorio),
    path('remover/', views.remover),
    path('visualizavoo/', views.visualizavoo),
    path('login/', views.login),
    path('monitoring/', views.monitoring),
    path('preenchimentoAtrasos/', views.preenchimentoAtrasos),
    path('preenchimentoCancelamentos/', views.preenchimentoCancelamentos),
    path('reports/', views.reports),
]
