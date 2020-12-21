from django.urls import path
from . import views
from .views import primeiraview, transferir, login

app_name = "banco_app"

urlpatterns = [
    #path('',primeiraview, name = 'primeiraview'),
    path('transferir/',transferir, name = 'transferir'),
    path('',login, name = 'login')
]