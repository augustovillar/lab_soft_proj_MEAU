from django import forms
from .models import Voo, Historico


class criaVoo(forms.ModelForm):

    class Meta:
        model = Voo
        fields = ['codigoVoo', 'companhia', 'destino', 'horarioPartidaProgramado', 'horarioChegadaProgramado', 'origem',]
        labels = {
            'codigoVoo':"Código Voo",
            'companhia': "Companhia",
            'destino': "Destino",
            'horarioPartidaProgramado': "Horário Partida",
            'horarioChegadaProgramado': "Horário Chegada",
            'origem': "Origem",
        }

class atualizaVoo(forms.ModelForm):

    class Meta:
        model = Voo
        fields = ['codigoVoo', 'companhia', 'destino', 'horarioPartidaProgramado', 'horarioChegadaProgramado', 'origem',]
        labels = {
            'codigoVoo':"Código Voo",
            'companhia': "Companhia",
            'destino': "Destino",
            'horarioPartidaProgramado': "Horário Partida",
            'horarioChegadaProgramado': "Horário Chegada",
            'origem': "Origem",
        }