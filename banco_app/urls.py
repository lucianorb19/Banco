from django.urls import path
from . import views
from .views import primeiraview, transferir, login, create, cadastro, mostrar_saldo,home

app_name = "banco_app"

urlpatterns = [
    #path('',primeiraview, name = 'primeiraview'),
    path('transferir/',transferir, name = 'transferir'),
    #path('',login, name = 'login'),
    path('create/', create, name='create'),
    path('cadastrar/', cadastro, name='cadastro'),
    path('saldo/',mostrar_saldo, name = 'mostrar_saldo'),
    #path('saldo/',mostrar_saldo, name = 'mostrar_saldo'),


    path('',home, name = 'home')
]