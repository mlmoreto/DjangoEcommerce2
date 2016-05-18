from django.contrib import admin
from .models import Game, Genre

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title', 'slug', 'price', 'stock', 'available', 'purchase_price', 'created']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['available', 'created']
    list_editable = ['price', 'stock']
    search_fields = ['title', 'description']

admin.site.register(Game, GameAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

admin.site.register(Genre, GenreAdmin)