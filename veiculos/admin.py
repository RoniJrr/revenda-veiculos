from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco')
    search_fields = ('marca', 'modelo')
