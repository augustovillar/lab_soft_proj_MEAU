from django import forms
from .models import Voo, Historico


class criaVoo(forms.ModelForm):

    class Meta:
        model = Voo
        fields = ['codigoVoo', 'companhia', 'origem',
                  'destino', 'horarioProgramado', ]
        labels = {
            'codigoVoo': "Código Voo",
            'companhia': "Companhia",
            'origem': "Origem",
            'destino': "Destino",
            'horarioProgramado': "Horário Programado",

        }


class criaHistorico(forms.ModelForm):

    class Meta:
        model = Historico
        fields = ['id', 'voo', 'data', 'horarioReal', 'status']
        labels = {
            'id': "Identificação",
            'voo': "Código do Voo",
            'data': "Data",
            'horarioReal': "Horário Real",
            'status': "Status",
        }
