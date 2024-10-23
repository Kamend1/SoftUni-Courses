from django.contrib import admin

from WorldOfSpeedAppExamPrep24022024.cars.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['type', 'model', 'year', 'price', 'owner',]