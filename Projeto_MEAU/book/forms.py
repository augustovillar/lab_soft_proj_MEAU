from django import forms
from .models import Voo, Historico


class criaVoo(forms.ModelForm):

      class Meta:
        model = Voo
        fields = ['codigoVoo', 'companhia', 'origem', 'destino', 'horarioProgramado', ]
        labels = {
            'codigoVoo':"Código Voo",
            'companhia': "Companhia",
            'origem': "Origem",
            'destino': "Destino",
            'horarioProgramado': "Horário Programado",
            
        }

