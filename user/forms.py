from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, required=True)
    username = forms.CharField(label='Apelido', max_length=100, required=True)
    password = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=100, required=True)
