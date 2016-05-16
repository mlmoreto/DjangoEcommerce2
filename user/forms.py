from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, required=True)
    username = forms.CharField(label='Apelido', max_length=100, required=True)
    password = forms.CharField(label='Senha', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    birthDate = forms.DateField(label='Data de Nascimento', required=True)
    fone = forms.CharField(label='Fone', required=True)
    cpf = forms.CharField(label='CPF', required=True)
    estado = forms.CharField(label='Estado', required=True)
    cidade = forms.CharField(label='Cidade', required=True)
    rua = forms.CharField(label='Rua', required=True)
    numero = forms.CharField(label='Número', required=True)

    def clean_username(self):
        data = self.cleaned_data['username']
        i = User.objects.filter(username=data).count()
        if i == 1:
            raise ValidationError(('Usuário já existe, tente outro apelido'), code='invalid')
            return False
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        i = User.objects.filter(email=data).count()
        if i == 1:
            raise ValidationError(('Email já foi utilizado, tente outro email'), code='invalid')
            return False
        return data

    def clean_birthDate(self):
        data = self.cleaned_data['birthDate']
        now = datetime.now().date()
        if (data < now):
            return data
        else:
            raise ValidationError(('Data inválida'), code='invalid')
            return False


class UserLogin(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)

    def clean_username(self):
        data = self.cleaned_data['username']
        i = User.objects.filter(username=data).count()
        if i == 0:
            raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')
            return False
        return data

    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username)[0]
        if (user.check_password(password)):
            return password
        else:
            raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')
