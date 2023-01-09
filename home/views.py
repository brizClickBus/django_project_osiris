from django.shortcuts import render
from .forms import Sign_in

# Create your views here.
def sign_in(request):
    return render(request,'home/sign_in.html',{'sign_in':Sign_in()})

def sign_out(request):
    pass

def sign_up(request):
    pass

