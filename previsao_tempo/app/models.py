from django.db import models

class MedicoesCidade(models.Model):
    # busca do html
    cidade = models.CharField(max_length=200, null=False, blank=False)
    sigla_pais = models.CharField(max_length=2, null=False, blank=False)

class DadosClimaticos(models.Model):
    data_medicao = models.CharField(max_length=10, null=False, blank=False)
    hora_medicao = models.CharField(max_length=10, null=True)
    nascer_sol = models.CharField(max_length=10, null=False, blank=False)
    por_sol = models.CharField(max_length=10, null=False, blank=False)
    temperatura_atual = models.FloatField(null=False, blank=False)
    temperatura_minima = models.FloatField(null=False, blank=False)
    temperatura_maxima = models.FloatField(null=False, blank=False)
    velocidade_vento = models.IntegerField(null=False, blank=False)
    umidade_relativa_ar = models.IntegerField(null=False, blank=False)
    volume_chuva = models.IntegerField(null=False, blank=False)
    detalhes = models.CharField(max_length=100, null=False, blank=False)
    medicoes_cidade = models.ForeignKey(MedicoesCidade, on_delete=models.CASCADE)




