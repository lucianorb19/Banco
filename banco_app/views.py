from django.shortcuts import render
from .forms import Tranferencias,Login
# Create your views here.

def primeiraview(request):
    return render(request, 'banco_app/index.html')

def transferir(request):
    form_tranferencia = Tranferencias() #VARIÁVEL FORM RECEBENDO INSTÂNCIA DA CLASSE TRANSFERENCIAS

    return render (request, 'banco_app/transferir.html',{'form_tranferencia':form_tranferencia})
                            #QUAL HTML SE CONECTA        PASSANDO FORM PARA A VIEW, PARA USAR NO HTML   

def login(request):
    form_login = Login(request.POST or None) #SE TIVER ALGO NA REQUEST, JÁ ENVIA O FORMULÁRIO PREENCHIDO

    senha_form=''   #VARIÁVEIS SERÃO PREENCHIDAS COM OS VALORES DO FORM
    login_form = ''

    if request.method == 'POST': #VARIÁVEIS TEM Q SER PASSADAS PELO MÉTODO POST NO FORMULÁRIO
        if form.is_valid(): #VALIDAÇÃO DOS DADOS
            senha_form = form.cleaned_data['senha_usu']#CAMPOS NO FORMS
            login_form = form.cleaned_data['login_usu']#CAMPOS NO FORMS
    return render (request, 'banco_app/login.html',{'form_login':form_login, 'senha_form':senha_form, 'login_form':login_form})