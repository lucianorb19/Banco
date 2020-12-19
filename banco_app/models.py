from django.db import models
#from cpf_field.models import CPFField

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length=11, help_text = "Somente números", unique = True)
    nascimento = models.DateField(help_text = "xx/xx/xxxx")

    #FUNÇÃO PARA MOSTRAR NA LISTA O NOME DO CLIENTE
    def __str__(self):
        return self.nome

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #CHAVE ESTRANGEIRA PARA CLIENTE
    numero_conta = models.CharField(max_length=10, help_text = "Digite os 10 Dígitos da conta") #10 DÍGITOS
    limite_conta = models.PositiveIntegerField # PADRÃO DE 200 REAIS DE LIMITE NA CONTA
    saldo_conta = models.PositiveIntegerField #PADRÃO DE 100 REAIS DE SALDO PARA ABERTURA DA CONTA

    def __str__(self):
        return self.numero_conta



#artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
'''
CLIENTE
Nome - charfield
CPF - 
Nascimento - Datefield


CONTA
Cliente - ForeignKey
Número da conta
Limite
Saldo


TRANSAÇÃO
Conta - ForeignKey
Cliente - ForeignKey
Tipo (Debito, Credito) - Choicefield [('Débito','Débito'),('Crédito','Crédito')]
Valor -

'''