from django.shortcuts import render
from .forms import UserForm, UserLogin
from .models import User
from django.contrib import auth


# Create your views here.

def show_user(request):
    dic = createForm(True)
    return render(request, 'userForm.html', dic)


def cadastro_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User()
            user.cidade = form.cleaned_data['cidade']
            user.birthDate = form.cleaned_data['birthDate']
            user.cpf = form.cleaned_data['cpf']
            user.email = form.cleaned_data['email']
            user.estado = form.cleaned_data['estado']
            user.fone = form.cleaned_data['fone']
            user.name = form.cleaned_data['name']
            user.numero = int(form.cleaned_data['numero'])
            user.rua = form.cleaned_data['rua']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            dic = {'mensagem': 'Cadastro',
                   'body': 'Foi um sucesso'}
            return render(request, 'userSucesso.html', dic)
        else:
            dic = createForm(False, formUser=form)
            return render(request, 'userForm.html', dic)
    else:
        dic = createForm(False)
        return render(request, 'userForm.html', dic)


def login_user(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            print('logou')##Ainda falta salvar o user logado na sessão.
        else:
            dic = createForm(True, formLogin=form)
            return render(request, 'userForm.html', dic)

        dic = createForm(True, formLogin=form)
        return render(request, 'userForm.html', dic)
    else:
        dic = createForm(True)
        return render(request, 'userForm.html', dic)


def createForm(active, formLogin=UserLogin(), formUser=UserForm()):
    dic = {'form': formUser,
           'formLogin': formLogin,
           'loginAtivoTab': 'active' if active else '',
           'cadastroAtivoTab': '' if active else 'active',
           'loginAtivo': ' in active' if active else '',
           'cadastroAtivo': '' if active else ' in active'
           }
    return dic;
