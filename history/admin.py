from daterange_filter.filter import DateRangeFilter
from django.contrib import admin

from .models import Pedido, Produto

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_display = ['user', 'data', 'total']
    list_filter = (
        ('data', DateRangeFilter),
    )
    search_fields = ['data']


admin.site.register(Pedido, PedidoAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido', 'game', 'quantidade', 'valorUnitario']

admin.site.register(Produto, ProdutoAdmin)