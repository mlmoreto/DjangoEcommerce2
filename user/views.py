from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm, UserLogin, UserRecuperar, UserAlterForm
from .models import User
from django.contrib.auth import login, authenticate, get_backends, logout
import random
from django.core.mail import send_mail
from snake_shop import settings
from django.contrib.auth.decorators import login_required


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
            user.password = form.cleaned_data['password']
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
            get_backends()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            if(user.is_password_generated):
                return HttpResponseRedirect(reverse('user.views.alterUser'))
            return HttpResponseRedirect(reverse('shop.views.home'))
        else:
            dic = createForm(True, formLogin=form)
            return render(request, 'userForm.html', dic)
    else:
        dic = createForm(True)
        return render(request, 'userForm.html', dic)


def createForm(active, formLogin=UserLogin(), formUser=UserForm(), formRecuperar=UserRecuperar()):
    dic = {'form': formUser,
           'formLogin': formLogin,
           'loginAtivoTab': 'active' if active else '',
           'cadastroAtivoTab': '' if active else 'active',
           'loginAtivo': ' in active' if active else '',
           'cadastroAtivo': '' if active else ' in active',
           'formRecuperar': formRecuperar
           }
    return dic


def deslogar(request):
    logout(request)
    return HttpResponseRedirect(reverse('shop.views.home'))


@login_required(login_url='/user/login/')
def minha_conta(request):
    if (isCliente(request.user)):
        return render(request, 'usuario_home.html')
    else:
        return HttpResponseRedirect(reverse('shop.views.home'))


@login_required(login_url='/user/login/')
def meu_carrinho(request):
    if (isCliente(request.user)):
        return render(request, 'usuario_carrinho.html')
    else:
        return HttpResponseRedirect(reverse('shop.views.home'))


@login_required(login_url='/user/login/')
def meu_historico(request):
    if (isCliente(request.user)):
        return render(request, 'usuario_historico.html')
    else:
        return HttpResponseRedirect(reverse('shop.views.home'))


@login_required(login_url='/user/login/')
def meus_dados(request):
    if (isCliente(request.user)):
        from .forms import UserAlterForm
        form = UserAlterForm()
        dic = {'form': setDados(user=request.user, form=form)}

        return render(request, 'usuario_dados.html', dic)
    else:
        return HttpResponseRedirect(reverse('shop.views.home'))

def setDados(user, form):
    form.fields['name'].initial = user.name
    form.fields['username'].initial = user.username
    data = datetime.strptime(str(user.birthDate), '%Y-%m-%d')
    form.fields['birthDate'].initial = data.strftime('%d/%m/%Y')
    form.fields['cidade'].initial = user.cidade
    form.fields['cpf'].initial = user.cpf
    form.fields['email'].initial = user.email
    form.fields['estado'].initial = user.estado
    form.fields['fone'].initial = user.fone
    form.fields['numero'].initial = user.numero
    form.fields['rua'].initial = user.rua
    form.user = user
    return form

def isCliente(user):
    return isinstance(user, User().__class__)

@login_required(login_url='/user/login/')
def alterUser(request):
    if (isCliente(request.user)):
        if (request.method == 'POST'):
            form = UserAlterForm(request.POST)
            form.user = request.user
            if(form.is_valid()):
                form.user.save()
                dic = {'mensagem': 'Alterar dados',
                   'body': 'Foi um sucesso!!'}
                return render(request, 'userSucesso.html', dic)
            else:
                dic = {'form': form}
                return render(request, 'usuario_dados.html', dic)
        else:
            return HttpResponseRedirect(reverse('user.views.meus_dados'))
    else:
        return HttpResponseRedirect(reverse('shop.views.home'))


def recuperarSenha(request):
    if request.method == 'POST':
        form = UserRecuperar(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            user.is_password_generated = True

            senha = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r',
                     't', 'y', 'u', 'i', 'o', 'p']
            random.shuffle(senha)
            newSenha = ''
            for c in senha[:7]:
                newSenha += c
            user.password = newSenha

            # email
            msg = ("Usuário: " + user.username + "\nSenha: " + user.password)
            to_list = [user.email]
            send_mail('Recuperação de Senha SNAKEGAMES', msg, settings.EMAIL_HOST_USER,
                      to_list, fail_silently=True)
            # fim

            user.save()
            dic = {'mensagem': 'Recuperar Senha',
                   'body': 'Foi um sucesso!!'}
            return render(request, 'userSucesso.html', dic)
        else:
            dic = createForm(True, formRecuperar=form)
            return render(request, 'userForm.html', dic)
    else:
        dic = createForm(True)
        return render(request, 'userForm.html', dic)
