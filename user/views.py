from django.shortcuts import render
from .forms import UserForm, UserLogin


# Create your views here.

def show_user(request):
    dic = createForm(True)
    return render(request, 'userForm.html', dic)


def cadastro_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and form.clean_username():
            pass
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
            pass
        else:
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
