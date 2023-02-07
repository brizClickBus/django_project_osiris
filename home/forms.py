from django import forms

class Forms_termos(forms.Form):
    aceite = forms.BooleanField()


class CadInfos(forms.Form):
    # infos bancarias
    numerobanco = forms.IntegerField(max_value=10, label='Número do banco')
    nomebanco = forms.CharField(max_length=225, label='Nome do banco')
    descricaobanco = forms.CharField(max_length=225, label='Nome do banco')

