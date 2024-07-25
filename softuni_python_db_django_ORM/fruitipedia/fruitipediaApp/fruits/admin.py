from django.contrib import admin

# Register your models here.
from fruitipediaApp.fruits.models import Category, Fruit


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'nutrition')
