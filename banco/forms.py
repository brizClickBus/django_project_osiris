from django import forms
from .models import Bancos,Cartoes,Limites,Cartao_alimentacao


class BancoForms(forms.ModelForm):
    class Meta:
        model = Bancos
        fields = ['nomebanco','descricao']


class CartoinsForms(forms.ModelForm):
    class Meta:
        model = Cartoes
        fields = "__all__"


class CartaoAlimentacaoForms(forms.ModelForm):
    class Meta:
        model = Cartao_alimentacao
        fields = "__all__"


class LimitesForms(forms.ModelForm):
    class Meta:
        model = Limites
        fields = "__all__"