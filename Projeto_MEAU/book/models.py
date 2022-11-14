from django.db import models
# Create your models here.

class Voo(models.Model):
    id = models.AutoField(primary_key=True)
    codigoVoo = models.CharField(max_length=14, unique=True) # this field must be unique throughout the table
    companhia = models.CharField(max_length=20)
    origem = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    horarioProgramado = models.TimeField(null=True)
    # horarioPartidaProgramado = models.TimeField(null=True)
    # horarioChegadaProgramado = models.TimeField(null=True)
    
    class Meta:
        db_table = 'voo'
    
    def __str__(self):
        return f'{self.codigoVoo}'

class Historico(models.Model):

    class Status(models.TextChoices):
            EMBARCANDO = 'EMBARCANDO'
            CANCELADO = 'CANCELADO'
            PROGRAMADO = 'PROGRAMADO'
            TAXIANDO = 'TAXIANDO'
            PRONTO = 'PRONTO'
            AUTORIZADO = 'AUTORIZADO'
            EM_VOO = 'EM_VOO'
            ATERRISSADO = 'ATERRISSADO'
            
    id = models.AutoField(primary_key=True)
    voo  = models.ForeignKey(Voo, null=True, on_delete=models.SET_NULL)
    data = models.DateField(null=True) #data referente ao aeroporto de SP - se o voo chegou é a data de chegada, se foi embora é a data de partida
    horarioReal = models.TimeField(null=True)
    # horarioPartidaReal = models.TimeField(null=True)
    # horarioChegadaReal = models.TimeField(null=True)
    status = models.CharField(choices=Status.choices, max_length=30, null=True)
    class Meta:
        db_table = 'historico'
    
    def __str__(self):
        return f'{self.voo}'