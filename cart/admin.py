from django.contrib import admin
from .models import Cart, Item

class ItemInline(admin.TabularInline):
    model = Item

class AdminCart(admin.ModelAdmin):
    list_display = ['user', 'update']
    date_hierarchy = 'update'
    search_fields = ['update']
    inlines = [ItemInline]

admin.site.register(Cart, AdminCart)

class AdminItem(admin.ModelAdmin):
    list_display = ['cart', 'game', 'quantidade']
    list_editable = ['quantidade']
    list_filter = ['cart']

admin.site.register(Item, AdminItem)