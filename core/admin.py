from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'e_mail', 'whatsapp')  # Colunas exibidas na lista
    search_fields = ('nome', 'e_mail', 'whatsapp')  # Campos de busca
    list_filter = ('e_mail',)  # Filtro por campo
    ordering = ('nome',)  # Ordenação padrão por nome

admin.site.register(Cliente, ClienteAdmin)
