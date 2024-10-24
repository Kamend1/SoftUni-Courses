from django.contrib import admin

from FruitipediaExamPrep2.fruits.models import Fruit


# Register your models here.
@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'nutrition', 'owner',]
