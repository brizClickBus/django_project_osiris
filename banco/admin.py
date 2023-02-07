from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Bancos)
admin.site.register(Extrato)
admin.site.register(Cartoes)
admin.site.register(Fatura)
admin.site.register(Bancos_cadastrados_bancoCental)