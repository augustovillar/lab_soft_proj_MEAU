from django.db import models

# Create your models here.
class Voo(models.Model):
    id_voo = models.IntegerField(primary_key=True)
    codigoVoo = models.CharField(max_length=12, null=False)
    aeroportoOrigem = models.CharField(max_length=200, null=False)
    aeroportoDestino = models.CharField(max_length=200, null=False)
    horarioPartidaProgramado = models.DateTimeField(null=False)
    horarioChegadaProgramado = models.DateTimeField(null=False)
    rota = models.CharField(max_length=10, null=False)
    companhia = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'voo'

class Historico(models.Model):
    id_historico = models.IntegerField(primary_key=True)
    historicoPartidaReal = models.DateTimeField(null=False)
    horarioChegadaReal = models.DateTimeField(null=False)
    data = models.DateTimeField(auto_now=False)
    estado = models.CharField(max_length=20, null=False)
    class Meta:
        db_table = 'historico'

#tabela da relação entre Voo e Historico (organização)
class Relacao(models.Model):
    id_historico = models.ForeignKey(Historico, on_delete=models.CASCADE)
    id_voo = models.ForeignKey(Voo, on_delete=models.CASCADE)