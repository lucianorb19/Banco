from django.contrib import admin
from .models import Cliente, Conta #IMPORTANDO MODEL CLIENTE PRA REGISTRAR NA PÁGINA DE ADMIN DJANGO

# Register your models here.

admin.site.register(Cliente) #REGISTRANDO MODEL CLIENTE NA PÁGINA ADMIN DJANGO
admin.site.register(Conta)


#@admin.register(Cliente)
#@admin.register(Conta)

'''
class ContaAdmin(admin.ModelAdmin):
    list_display = ("numero_conta","saldo") #INFORMAÇÕES MOSTRADAS NA LISTA DA CONTA
    prepopulated_fields = {"limite_conta" : (200,),
                           "saldo_conta" : (100, )} #PREENCHE AUTOMATICAMENTE O CAMPO LIMITE E SALDO
'''                                              
