from django import forms

class Tranferencias(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino',max_length=100)
    valor = forms.FloatField(label='Valor')

class Login(forms.Form):
    login_usu = forms.CharField(label='Usuário',max_length=100)
    senha_usu = forms.CharField(label='Senha',max_length=50)