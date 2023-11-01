from django.contrib import admin

# Register your models here.

from AgendaApp.models import Contato,Cidade

class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ['id','nome','apelido','data_nascimento',"estado_civil",'estado','cidade']
    list_filter = ['id','nome','data_nascimento','cidade', 'estado']
    search_fields= ['id','nome', 'apelido']







admin.site.register(Contato,ContatoAdmin)
admin.site.register(Cidade)