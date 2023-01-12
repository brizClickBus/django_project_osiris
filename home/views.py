from django.shortcuts import render,redirect
from .forms import Sign_in,Sign_up
from .models import SignUp

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        pass

    return render(request,'home/sign_in.html',{'sign_in':Sign_in()})

def sign_out(request):
    if request.method == 'POST':
        pass

def sign_up(request):
    return render(request,'home/sign_up.html',{'sign_up':Sign_up()})