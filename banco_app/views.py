from django.shortcuts import render,redirect
from .forms import Tranferencias,Login,Cliente_form, Menu
from . import models
# Create your views here.

def primeiraview(request):#NÃO USA
    return render(request, 'banco_app/index.html')

def transferir(request):#NÃO USA
    form_tranferencia = Tranferencias() #VARIÁVEL FORM RECEBENDO INSTÂNCIA DA CLASSE TRANSFERENCIAS

    return render (request, 'banco_app/transferir.html',{'form_tranferencia':form_tranferencia})
                            #QUAL HTML SE CONECTA        PASSANDO FORM PARA A VIEW, PARA USAR NO HTML   

def login(request):#NÃO USA
    form_login = Login(request.POST or None) #SE TIVER ALGO NA REQUEST, JÁ ENVIA O FORMULÁRIO PREENCHIDO

    senha_form=''   #VARIÁVEIS SERÃO PREENCHIDAS COM OS VALORES DO FORM
    login_form = ''

    if request.method == 'POST': #VARIÁVEIS TEM Q SER PASSADAS PELO MÉTODO POST NO FORMULÁRIO
        if form.is_valid(): #VALIDAÇÃO DOS DADOS
            senha_form = form.cleaned_data['senha_usu']#CAMPOS NO FORMS
            login_form = form.cleaned_data['login_usu']#CAMPOS NO FORMS
    return render (request, 'banco_app/login.html',{'form_login':form_login, 'senha_form':senha_form, 'login_form':login_form})


#CRIA FORMULÁRIO DE CADASTRO PARA CLIENTE E SALVA INFORMAÇÕES NO FORMULÁRIO form_cadastro_usuario
def cadastro(request):
    form_cadastro_usuario = Cliente_form() #VARIÁVEL FORM RECEBENDO INSTÂNCIA DA CLASSE TRANSFERENCIAS

    return render (request, 'banco_app/cadastrar.html',{'form_cadastro_usuario':form_cadastro_usuario})

#INSERE INFORMAÇÕES DE form_cadastro_usuario EM CLIENTE E SALVA NO BD
def create(request):
    cliente = models.Cliente(nome=request.POST['nome'],cpf=request.POST['cpf'],nascimento=request.POST['nascimento'])
    conta = models.Conta(cliente=cliente ,numero_conta='00'+cliente.cpf,limite_conta=200, saldo_conta=100)
    cliente.save()
    conta.save()

    return redirect('') #REDIRECIONA PRA HOME

def home(request):
    form_menu = Menu()

    return render (request, 'banco_app/menu.html',{'form_menu':form_menu})  

def mostrar_saldo(request):
    id = request.POST['id'] #OBTENDO DADOS DO FORM PREENCHIDO EM HOME
    cliente = models.Cliente.objects.get(id = id) #OBTENDO DADO DO BANCO DO CLIENTE COM ID PASSADO NA LINHA ACIMA
    conta = models.Conta.objects.get(cliente_id = id) #MESMA COISA, MAS PRA CONTA

    return render (request, 'banco_app/saldo.html',{'cliente':cliente, 'conta': conta})
