from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Добавьте другие настройки админки по необходимости

# Здесь вы регистрируете модель CustomUser, а не CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)