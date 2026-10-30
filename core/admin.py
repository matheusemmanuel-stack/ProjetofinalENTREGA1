from django.contrib import admin
from .models import Corte, Agendamento


@admin.register(Corte)
class CorteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'ativo')
    ordering = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'data', 'horario', 'corte')
    list_filter = ('data', 'corte')
    search_fields = ('nome_cliente',)
    ordering = ('data', 'horario')
