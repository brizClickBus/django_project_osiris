from django.shortcuts import render,redirect
from .forms import Sign_in,Sign_up
from django.contrib import auth, messages
from django.contrib.auth.models import User
# Create your views here.
def sign_in(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        password = request.POST['password']
        
        if username =="" or password == "":
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return render(request,'users/sign_in.html',{'sign_in':Sign_in()})
        
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
        else:
            messages.error(request,'Usuário não cadastrado')
            return render(request,'users/sign_in.html',{'sign_in':Sign_in()})
    messages.success(request,"Seja Bem-vindo!")
    return render(request,'users/sign_in.html',{'sign_in':Sign_in()})

def sign_out(request):
    auth.logout(request)
    messages.error(request,'Espero ter ajudado!')
    return render(request,'users/sign_in.html',{'sign_in':Sign_in()})
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repeatPassWord = request.POST['repeatPassWord']
        
        if not first_name.split():
            messages.error(request,"seu nome esta em branco ou invalido")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        if len(password) < 8:
            messages.error(request,"Use uma senha com 8 ou mais caracteres")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        elif not any(chr.isdigit() for chr in password):
            messages.error(request,"Bola uma senha com algum número no meio")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        elif not any(x.isupper() for x in password):
            messages.error(request,"Bola uma senha com alguma letra maiúscula")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        else:
            # checar caracteres especiais
            chars = """ !@#$%ˆ&*()_+-[]{"};'\:|,./<>?:| """
            resultsPassword=[]
            for char in list(chars):
                if password.find(char) >= 0:
                    resultsPassword.append(1)
                else:
                    resultsPassword.append(0)
            if sum(resultsPassword) == 0:
                messages.error(request,"Bola uma senha com algum caractere especial")
                return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        if password != repeatPassWord:
            messages.error(request,"as senhas não conferem!")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        #autenticar se usuario ja tem cadastro no banco de dados 
        if User.objects.filter(email=email).exists():
            messages.error(request,"esse E-Mail já está cadastrado")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
                #autenticar se o userName ja tem cadastro no banco de dado
        
        if len(username.split()) > 1:
            messages.error(request,"userName não pode ter espaços")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"esse userName já está cadastrado")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
        
        try:
            if len(first_name.split()) > 1:
                messages.error(request,"O campo primeiro nome não pode ter espaços e nem seu nome completo")
                return render(request,'users/sign_up.html',{'sign_up':Sign_up()})
            else:
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password)
                messages.success(request,f"Bem vindo, {first_name} {last_name}, fico feliz que você escolheu o Osiris para tomar conta do seu dinheiro!")
                return render(request,'users/sign_in.html',{'sign_in':Sign_in()})
        except:
            messages.error(request,"Problemas na criação do seu cadastro, por gentileza atualize a pagina e tente novamente")
            return render(request,'users/sign_up.html',{'sign_up':Sign_up()})

    # != POST    
    else:
        return render(request,'users/sign_up.html',{'sign_up':Sign_up()})