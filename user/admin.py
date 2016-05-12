from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'data', 'birthDate']
    prepopulated_fields = {'username': ('name',)}

admin.site.register(User, UserAdmin)