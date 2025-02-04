from django.contrib import admin
from .models import Category, User, Software

# Настройка отображения для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Отображаем поля 'name' и 'description'
    search_fields = ('name',)  # Возможность поиска по имени категории

# Настройка отображения для модели User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # Отображаем поля 'username' и 'email'
    list_filter = ('email',)  # Фильтрация по полю email
    search_fields = ('username',)  # Возможность поиска по имени пользователя

# Настройка отображения для модели Software
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'release_date')  # Отображаем основные поля
    list_filter = ('category', 'release_date')  # Фильтрация по категории и дате выпуска
    search_fields = ('name',)  # Возможность поиска по названию программы

# Регистрируем модели с их настройками
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Software, SoftwareAdmin)
