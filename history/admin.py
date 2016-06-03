from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg
from .models import Pedido, Produto


# Register your models here.
class TotalPedido(ChangeList):
    fields_to_total = ['total']

    def get_total_values(self, queryset):
        total = Pedido()
        total.custom_alias_name = "Total: "
        for field in self.fields_to_total:
            print(queryset.aggregate(Sum(field))['total__sum'])
            setattr(total, field, queryset.aggregate(Sum(field))['total__sum'])
        return total

    def get_results(self, request):
        super(TotalPedido, self).get_results(request)
        total = self.get_total_values(self.get_queryset(request))
        len(self.result_list)
        self.result_list._result_cache.append(total)


class ProdutoInline(admin.TabularInline):
    model = Produto


class PedidoAdmin(admin.ModelAdmin):
    date_hierarchy = 'data'
    list_display = ['user', 'data', 'total']
    list_filter = (
        ('data', DateRangeFilter),
    )
    search_fields = ['data']
    inlines = [ProdutoInline]

    def get_changelist(self, request, **kwargs):
        return TotalPedido


admin.site.register(Pedido, PedidoAdmin)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'game', 'quantidade', 'valorUnitario']


admin.site.register(Produto, ProdutoAdmin)
