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
        try:
            data = self.cleaned_data['username']
            i = User.objects.filter(username=data).count()
            if i == 0:
                raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')
            return data
        except:
            raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')

    def clean_password(self):
        try:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = User.objects.filter(username=username)[0]
            if (user.check_password(password)):
                return password
            else:
                raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')
        except:
            raise ValidationError(('Erro usuário ou senha incorreta'), code='invalid')

class UserRecuperar (forms.Form):
    email = forms.CharField(label='Email', max_length=100, required=True)

    def clean_email(self):
        try:
            data = self.cleaned_data['email']
            i = User.objects.filter(email=data).count()
            if( i == 1):
                return data
            else:
                raise ValidationError(('Erro email não encontrado'), code='invalid')
        except:
            raise ValidationError(('Erro email não encontrado'), code='invalid')

class UserAlterForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, required=True)
    username = forms.CharField(label='Apelido', max_length=100, required=True)
    password = forms.CharField(label='Senha', max_length=100, required=False)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    birthDate = forms.DateField(label='Data de Nascimento', required=True)
    fone = forms.CharField(label='Fone', required=True)
    cpf = forms.CharField(label='CPF', required=True)
    estado = forms.CharField(label='Estado', required=True)
    cidade = forms.CharField(label='Cidade', required=True)
    rua = forms.CharField(label='Rua', required=True)
    numero = forms.CharField(label='Número', required=True)

    user = None

    def clean_name(self):
        data = self.cleaned_data['name']
        if(data != self.user.name):
            self.user.name = data
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if(data != self.user.username):
            i = User.objects.filter(username=data).count()
            if i == 1:
                raise ValidationError(('Usuário já existe, tente outro apelido'), code='invalid')
                return False
            self.user.username = data
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if(len(data) > 0):
            self.user.password = data
            self.user.is_password_generated = False
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if(self.user.email != data):
            i = User.objects.filter(email=data).count()
            if i == 1:
                raise ValidationError(('Email já foi utilizado, tente outro email'), code='invalid')
                return False
            self.user.email = data
        return data

    def clean_birthDate(self):
        data = self.cleaned_data['birthDate']
        if(self.user.birthDate != data):
            now = datetime.now().date()
            if (data < now):
                self.user.birthDate = data
                return data
            else:
                raise ValidationError(('Data inválida'), code='invalid')
                return False

    def clean_fone(self):
        data = self.cleaned_data['fone']
        if(data != self.user.fone):
            self.user.fone = data
        return data

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        if(data != self.user.cpf):
            self.user.cpf = data
        return data

    def clean_estado(self):
        data = self.cleaned_data['estado']
        if(data != self.user.estado):
            self.user.estado = data
        return data

    def clean_cidade(self):
        data = self.cleaned_data['cidade']
        if(data != self.user.cidade):
            self.user.cidade = data
        return data

    def clean_rua(self):
        data = self.cleaned_data['rua']
        if(data != self.user.rua):
            self.user.rua = data
        return data

    def clean_numero(self):
        data = self.cleaned_data['numero']
        if(data != self.user.numero):
            self.user.numero = data
        return data