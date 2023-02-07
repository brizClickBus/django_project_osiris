from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class  Bancos_cadastrados_bancoCental(models.Model):
    ispb = models.IntegerField()
    name = models.CharField(max_length=250)
    code = models.FloatField()
    fullName = models.CharField(max_length=250)
    lastUpdate = models.DateTimeField()


class Bancos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    banks = models.ForeignKey(Bancos_cadastrados_bancoCental, on_delete=models.CASCADE)
    nomebanco = models.CharField(max_length=225)
    numerobanco = models.FloatField()
    descricao = models.CharField(max_length=225)
    createdAt = models.DateTimeField()


class Cartoes(models.Model):
    creditoChoices = (('SIM','Sim'),('NAO','Não'),('OS DOIS','Os dois'))
   
    banco = models.ForeignKey(Bancos, on_delete=models.CASCADE)
    nometitular = models.CharField(max_length=225)
    debtocredito = models.CharField(max_length=20,choices=creditoChoices)
    createdAt = models.DateTimeField()


class Cartao_alimentacao(models.Model):
    tipoChoices = (('VR','VR'),('VA','VA'),('CRÉDITO','Crédito'),('OUTROS','Outros'))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=225)
    tipo = models.CharField(max_length=20,choices=tipoChoices)
    createdAt = models.DateTimeField()


class Entradas_alimentacao(models.Model):
    cartao = models.ForeignKey(Cartao_alimentacao, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dataEntrada = models.DateTimeField()
 

class Extrado_alimentacao(models.Model):
    cartao = models.ForeignKey(Cartao_alimentacao, on_delete=models.CASCADE)


class Limites(models.Model):
    cartao = models.OneToOneField(Cartoes, on_delete=models.CASCADE)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    chequeEspecial = models.DecimalField(max_digits=10, decimal_places=2)

class Seguimento(models.Model):
    seguimentoChoice = (("ENTRADA","Entrada"),("SAIDA","Saida"))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20,choices=seguimentoChoice)
    createdAt = models.DateTimeField()


class Extrato(models.Model):
    pagamentoChoice = (("DINHEIRO","Dinheiro"),("CARTAO","Cartão"),("PIX","Pix"))
    
    seguiento = models.ForeignKey(Seguimento, on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartoes, on_delete=models.CASCADE)
    
    pagamento = models.CharField(max_length=20,choices=pagamentoChoice)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()

class Fatura(models.Model):
    
    seguiento = models.ForeignKey(Seguimento, on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartoes, on_delete=models.CASCADE)
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()