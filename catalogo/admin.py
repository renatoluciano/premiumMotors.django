from django.contrib import admin
from .models import Marca, Veiculo

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    # Colunas que vão aparecer na tabela de listagem de carros
    list_display = ('marca', 'modelo', 'ano_modelo', 'preco', 'estado', 'quilometragem', 'criado_em')
    
    # Filtros rápidos na barra lateral direita do painel
    list_filter = ('estado', 'marca', 'ano_modelo', 'portas')
    
    # Campos de busca por texto (barra de pesquisa)
    search_fields = ('modelo', 'versao', 'descricao')
    
    # Organiza os campos na hora de cadastrar ou editar um carro
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('marca', 'modelo', 'versao', 'estado')
        }),
        ('Especificações Técnicas', {
            'fields': ('ano_fabricacao', 'ano_modelo', 'cor', 'portas', 'quilometragem')
        }),
        ('Valores e Mídia', {
            'fields': ('preco', 'imagem_principal')
        }),
        ('Detalhes Adicionais', {
            'fields': ('descricao',),
            'classes': ('collapse',), # Deixa a descrição recolhida por padrão
        }),
    )
