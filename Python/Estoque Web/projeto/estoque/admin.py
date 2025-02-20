from django.contrib import admin
from .models import Estoque, EstoqueItens
# Register your models here.

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'funcionario',
        'nf',
        'movimento',
    )
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'