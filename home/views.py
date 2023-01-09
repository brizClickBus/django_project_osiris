from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request,'home/sign_in.html')

def sign_out(request):
    pass

def sign_up(request):
    pass

