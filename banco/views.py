import json
from datetime import datetime

import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import BancoForms,CartoinsForms,LimitesForms,CartaoAlimentacaoForms
from .models import Bancos,Bancos_cadastrados_bancoCental,Cartao_alimentacao,Cartoes

def ajax(request,model):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        q = request.GET.get('term', '')

        if model == "Bancos_cadastrados_bancoCental":
            lista = Bancos_cadastrados_bancoCental.objects.filter(name__icontains=q)
        elif model == "Bancos_usuario":
            lista = Bancos.objects.filter(name__icontains=q)

        data = ajax_results(lista)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def ajax_results(lista):
        results = []
        for item in lista:
            return_json = {}
            return_json['label'] = item.name
            return_json['value'] = item.name
            results.append(return_json)
        return json.dumps(results)


def height_table(df):
    try:
        df = df.to_dict('recording')
        tamanhoTh = len(df)*40+75
        if tamanhoTh > 200:
            tamanhoTh = 200
        return {'df':df,'height':tamanhoTh}
    except:
        return False


# Create your views here.
@login_required
def cad_banco(request):
    bancoForms = BancoForms()
    if request.method == 'POST':
        if request.POST.get('save_banco_and_add_another'):
            nomebanco = request.POST['nomebanco']
            try:
                if Bancos_cadastrados_bancoCental.objects.filter(name=nomebanco).exists():
                    user_banco = Bancos()
                    bancosCadastrados = list(Bancos_cadastrados_bancoCental.objects.filter(name=nomebanco).all().values())[0]
                    user_banco.user_id = request.user.id
                    user_banco.banks_id = bancosCadastrados['id']
                    user_banco.nomebanco = nomebanco
                    user_banco.numerobanco = bancosCadastrados['code']
                    user_banco.descricao = request.POST['descricao']
                    user_banco.createdAt = datetime.now()
                    user_banco.save()
                    
                    df = pd.DataFrame(list(Bancos.objects.filter(user_id=request.user.id).all().values())) 
                    df = df.drop(columns=["createdAt"])
                    table = height_table(df)

                    messages.success(request,'Banco cadastrado com sucesso!')
                    return render(request,'cad/banco.html',{"bancoforms":bancoForms,"bancosSalvos":table['df'],"height":table['tamanho']})

                else:
                    messages.error(request,f'{nomebanco} : não foi encontrado na lista de bancos cadastrados do Banco Central')
            
            except:
                messages.error(request,f'Falha ao cadastrar o banco: {request.POST["nomebanco"]} tente novamente mais tarde')

            return render(request,'cad/banco.html',{"bancoforms":bancoForms})
    
        elif request.POST.get('next'):
            return redirect('cad_cartoes')
    else:
        table = height_table(request)
        return render(request,'cad/banco.html',{
            "bancoforms":bancoForms,
            "bancosSalvos":table['df'],
            "height":table['height']
            }
        )



def cad_cartoes(request):
    models_banco = Bancos.objects.filter(user_id = request.user.id)
    if not models_banco.exists():
        messages.error(request,f'Cadastre pelo menos um banco para porder proseguir')
        redirect('cad_banco')
    else:
        cartoesForms = CartoinsForms()
        limiteForms = LimitesForms()
        cartaoAlimentacao = CartaoAlimentacaoForms()
       
        df_bancos = pd.DataFrame(list(models_banco.all().values()))
        
        list_of_bancos = list(df_bancos['nomebanco'])

    if request.method == 'POST':
        pass
    else:
        return render(request,'cad/banco.html',{
            "cartoesForms":cartoesForms,
            "cartaoAlimentacao":cartaoAlimentacao,
            "limiteForms":limiteForms,
            # "bancosSalvos":table['df'],
            # "height":table['tamanho'],
            "listaBancos":list_of_bancos
            }
        )