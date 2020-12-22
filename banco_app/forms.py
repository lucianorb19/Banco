from django import forms

class Tranferencias(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino',max_length=100)
    valor = forms.FloatField(label='Valor')

class Login(forms.Form):
    login_usu = forms.CharField(label='Usuário',max_length=100)
    senha_usu = forms.CharField(label='Senha',max_length=50)

class Cliente_form(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=100)
    nascimento = forms.CharField(label='Nascimento', max_length=100)

class Menu(forms.Form):
    id = forms.IntegerField(label='Código Cliente')