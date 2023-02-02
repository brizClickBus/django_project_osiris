from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seguimentos(models.Model):
    choice_seguiento = (('FIXO','Fixo'),('VARIADO','Variado'))
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225)
    tipo_seguimento = models.CharField(max_length=10,choices=choice_seguiento)

class Extrato(models.Model):
    seguimento = models.CharField(max_length=225) #fk para tabela Seguimentos
    value = models.DecimalField(max_digits=10,decimal_places=2)
    forma_pagamento = models.CharField(max_length=225)
    tipo_gasto = models.BooleanField() #1=Entrada 0=Saida
    date = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    