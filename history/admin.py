from django.contrib import admin
from .models import Pedido, Produto

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_display = ['user', 'data', 'total']

admin.site.register(Pedido, PedidoAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido', 'game', 'quantidade', 'valorUnitario']

admin.site.register(Produto, ProdutoAdmin)