from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario').strip()
        senha = request.POST.get('senha').strip()
        bdUsuario = authenticate(username=usuario, password=senha)
        if bdUsuario is None:
            messages.error(request, 'Usuário não encontrado')
            return redirect('login')
        else:
            auth.login(request, bdUsuario)
            return redirect('home')

    else:
        return render(request, 'login/index.html')


def cadastro(request):
    
    if request.method == 'POST':
        nome = request.POST.get('nome').strip()
        sobrenome = request.POST.get('sobrenome').strip()
        usuario = request.POST.get('usuario').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()
        senha2 = request.POST.get('senha2').strip()

        if len(nome.strip()) <= 3:
            messages.error(request, 'Nome muito curto')
            return redirect('cadastro')

        elif len(sobrenome) <= 3:
            messages.error(request, 'sobrenome muito curto')
            return redirect('cadastro')

        elif len(usuario) <= 3:
            messages.error(request, 'Usuário muito curto')
            return redirect('cadastro')

        elif len(senha) <= 3:
            messages.error(request, 'Senha muito curto')
            return redirect('cadastro')

        elif len(senha2) <= 3:
            messages.error(request, 'Senha muito curto')
            return redirect('cadastro')

        elif senha != senha2:
            messages.error(request, 'Senhas não são iguais')
            return redirect('cadastro')

        else:
            try:
                User.objects.create(
                    first_name=nome,
                    last_name=sobrenome,
                    username=usuario,
                    email=email,
                    password=make_password(senha),
                )
                return redirect('login')
            except:
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

    else:
        return render(request, 'cadastro/index.html')


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home/index.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
