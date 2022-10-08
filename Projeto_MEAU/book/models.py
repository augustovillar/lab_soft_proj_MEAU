from django.db import models

class Voo(models.Model):
    codigoVoo                = models.CharField(max_length = 12, primary_key = True)
    aeroportoOrigem          = models.CharField(max_length = 200, null = False)
    aeroportoDestino         = models.CharField(max_length = 200, null = False)
    horarioPartidaProgramado = models.DateTimeField(null = False)
    horarioChegadaProgramado = models.DateTimeField(null = False)
    rota                     = models.CharField(max_length = 10, null = False)
    companhia                = models.CharField(max_length = 200, null = False)

    class Meta:
        db_table = 'voo'

class Historico(models.Model):
    chaveVoo           = models.ForeignKey(Voo, on_delete = models.CASCADE)
    id_historico       = models.IntegerField(primary_key = True)
    horarioPartidaReal = models.DateTimeField(null = False)
    horarioChegadaReal = models.DateTimeField(null = False)
    data               = models.DateTimeField(auto_now = False)
    estado             = models.CharField(max_length = 20, null = False)

    class Meta:
        db_table = 'historico'