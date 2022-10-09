from django.db import models
import datetime
# Create your models here.

class Voo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigoVoo = models.CharField(max_length=12, null=False, unique=True) # this field must be unique throughout the table
    origem = models.CharField(max_length=30, null=True)
    destino = models.CharField(max_length=30, null=True)
    horarioPartidaProgramado = models.TimeField(null=True)
    horarioChegadaProgramado = models.TimeField(null=True)
    companhia = models.CharField(max_length=200, null=False)
    class Meta:
        db_table = 'voo'

class Historico(models.Model):
    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True) #data referente ao aeroporto de SP - se o voo chegou é a data de chegada, se foi embora é a data de partida
    horarioPartidaReal = models.TimeField(null=True)
    horarioChegadaReal = models.TimeField(null=True)
    status = models.CharField(max_length=30, null=True)
    class Meta:
        db_table = 'historico'