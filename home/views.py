from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Forms_termos

@login_required
def home(request):
    return render(request,'home/home.html')


@login_required
def termos(request):
    if request.method == 'POST':
        pass
    return render(request,'home/termos.html',context={"termos":Forms_termos()})