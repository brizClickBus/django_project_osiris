# import requests


# from datetime import datetime
# from banco.models import Bancos_cadastrados_bancoCental

# url = "https://brasilapi.com.br/api/banks/v1"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("A requisição falhou")

# bancos = Bancos_cadastrados_bancoCental()
# for banco in data:
#     if banco['code'] == None:
#         code = 0
#     else:
#         code = banco['code']
#     Bancos_cadastrados_bancoCental.objects.create(
#         ispb=banco['ispb'],
#         name = banco['name'],
#         code = code,
#         fullName = banco['fullName'],
#         lastUpdate = timezone.now()
#     )

#     bancos.ispb = banco['ispb']
#     bancos.name = banco['name']
#     if banco['code'] == None:
#         bancos.code = 0
#     else:
#         bancos.code = banco['code']

#     bancos.fullName = banco['fullName']
#     bancos.lastUpdate = timezone.now()
#     bancos.save()

# class  Banks(models.Model):
#     ispb = models.IntegerField(max_length=10)
#     name = models.CharField(max_length=250)
#     code = models.FloatField()
#     fullName = models.CharField(max_length=250)
