from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'data', 'birthDate', 'last_login', 'estado']
    prepopulated_fields = {'username': ('name',)}
    list_filter = ['data', 'birthDate', 'last_login', 'estado']
    search_fields = ['name', 'username', 'email', 'estado', 'cidade']
admin.site.register(User, UserAdmin)