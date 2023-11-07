from django.contrib import admin

# Register your models here.

from AgendaApp.models import Contato,Cidade,Telefone,Interesse


class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1

class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ['id','nome','apelido','data_nascimento','estado_civil','estado','cidade']
    list_display_links = ['id','nome']
    list_filter = ['id','nome','data_nascimento','cidade', 'estado',]
    search_fields= ['id','nome', 'apelido']
    inlines = [Telefones]
    filter_horizontal =['interesses']

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['ddd','numero','tipo','IsWatsApp']



admin.site.register(Contato,ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone,TelefoneAdmin)
admin.site.register(Interesse)
