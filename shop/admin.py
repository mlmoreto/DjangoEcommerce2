from django.contrib import admin
from .models import Game, Genre

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Game, GameAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Genre, GenreAdmin)