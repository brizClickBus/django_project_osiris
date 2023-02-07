from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Forms_termos
from .models import Termos

@login_required
def home(request):
    return render(request,'home/home.html')


@login_required
def termos(request):
    if request.method == 'POST':
        if Termos.objects.filter(user_id=request.user.id).exists():
            return redirect('cad_banco')    
        else:
            termos = Termos()
            if request.method == 'POST':
                if request.POST['aceite'] == 'on':
                    termos.aceito = 1
                else:
                    termos.aceito = 0
            termos.user = request.user
            termos.save()
            return redirect('cad_banco')
    else:
        return render(request,'home/termos.html',context={"termos":Forms_termos()})
