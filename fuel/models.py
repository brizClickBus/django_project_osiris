from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Cars(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20,null=True)
    marca =  models.CharField(max_length=225,null=True)
    modelo = models.CharField(max_length=50,null=True)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    apelido = models.CharField(max_length=100)
    createdAt = models.DateTimeField()

class Fuel(models.Model):
    cars = models.OneToOneField(Cars, on_delete=models.CASCADE)
    quilometragem_atual = models.DecimalField(max_digits=10,decimal_places = 2)
    preco_litro = models.DecimalField(max_digits=10,decimal_places = 2)
    tanque_cheio = models.BooleanField(null=True)
    total_pago = models.DecimalField(max_digits=10,decimal_places = 2)
    date = models.DateTimeField()
    seguimentos = models.CharField(default="gasolina",max_length=225)
    month = models.IntegerField()
    year = models.IntegerField()
