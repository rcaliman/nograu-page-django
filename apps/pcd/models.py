from django.db import models

class ModelPCD(models.Model):
    class Meta:
        verbose_name = 'Dados para calcular PCD'
        verbose_name_plural = verbose_name
    codigo_banco = models.CharField(max_length=10)
    proxima_parcela = models.CharField(max_length=10)
    ultima_parcela = models.CharField(max_length=10)
    quantidade_parcelas = models.CharField(max_length=10)
    valor_parcela = models.CharField(max_length=20)
    valor_emprestado = models.CharField(max_length=20)
    data_calculo = models.DateField(auto_now_add=True)

