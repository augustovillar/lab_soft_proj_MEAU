from django.db import models

class Voo(models.Model):
    id = models.AutoField(primary_key=True)
    codigoVoo = models.CharField(max_length=14, unique=True)
    companhia = models.CharField(max_length=20)
    origem = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    horarioProgramado = models.TimeField(null=True)
    
    class Meta:
        db_table = 'voo'
    
    def __str__(self):
        return f'{self.codigoVoo}'

class Historico(models.Model):

    class Status(models.TextChoices):
            PREVISTO = 'PREVISTO'
            EMBARCANDO = 'EMBARCANDO'
            CANCELADO = 'CANCELADO'
            PROGRAMADO = 'PROGRAMADO'
            TAXIANDO = 'TAXIANDO'
            PRONTO = 'PRONTO'
            AUTORIZADO = 'AUTORIZADO'
            EM_VOO = 'EM_VOO'
            ATERRISSADO = 'ATERRISSADO'
            
    id = models.AutoField(primary_key=True)
    voo  = models.ForeignKey(Voo, on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True)
    horarioReal = models.TimeField(null=True)
    status = models.CharField(choices=Status.choices, max_length=30, null=True)
    class Meta:
        db_table = 'historico'
    def __str__(self):
        return f'{self.voo}'