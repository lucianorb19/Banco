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
    limite_conta = models.DecimalField(max_digits=15, decimal_places=2,default=200) # PADRÃO DE 200 REAIS DE LIMITE NA CONTA
    saldo_conta = models.DecimalField(max_digits=15, decimal_places=2,default=100) #PADRÃO DE 100 REAIS DE SALDO PARA ABERTURA DA CONTA

    #CLIENTE - CONTA - SALDO - LIMITE
    def __str__(self):
        return f'{self.cliente}-----Número:{self.numero_conta}-----Saldo:{self.saldo_conta}-----Limite:{self.limite_conta}'

class Transacao(models.Model):
    TIPOS_TRANSACOES = [('Débito','Débito'),
                        ('Crédito','Crédito')]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_transacao = models.CharField(max_length=10, choices=TIPOS_TRANSACOES)
    valor = models.DecimalField(max_digits=15, decimal_places=2,default=0)

    def __str__(self):
        return f'Conta:{self.conta}-----Valor Transação:{self.valor}-----Tipo:{self.tipo_transacao}'




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