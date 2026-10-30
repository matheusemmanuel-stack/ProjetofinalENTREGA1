from django.contrib import admin
from .models import Corte


@admin.register(Corte)
class CorteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'ativo')
    ordering = ('nome',)